from OpenGL import GL
from array import array
import ctypes
import glfw
import glm
import math

VERTEX_SHADER = """
#version 400

layout(location=0)in vec3 attr_posicao;
layout(location=1)in vec3 attr_cor;

uniform mat4 mvp;
out vec3 cor;

void main(void) 
{
    cor = attr_cor;
    gl_Position = mvp * vec4(attr_posicao,1.0f);
}
"""

FRAGMENT_SHADER = """
#version 400

in vec3 cor;
out vec4 color;

void main(void) 
{
    color = vec4(cor,1.0f);
}
"""
def compilaShaders():
    error = None
    progId = GL.glCreateProgram()
    for type, source in [ (GL.GL_VERTEX_SHADER, VERTEX_SHADER), (GL.GL_FRAGMENT_SHADER, FRAGMENT_SHADER) ]:
        shaderId = GL.glCreateShader(type)
        GL.glShaderSource(shaderId,[source])
        GL.glCompileShader(shaderId)
        status = GL.glGetShaderiv(shaderId,GL.GL_COMPILE_STATUS)
        if not status:
            error = GL.glGetShaderInfoLog(shaderId)
            GL.glDeleteShader(shaderId)
            break
        else:
            GL.glAttachShader(progId,shaderId)
    if error == None:
        GL.glLinkProgram(progId)
        status = GL.glGetProgramiv(progId,GL.GL_LINK_STATUS)
        if not status:
            error = GL.glGetProgramInfoLog(progId)
        else:
            return progId
    for shaderId in GL.glGetAttachedShaders(progId):
        GL.glDetachShader(progId, shaderId)
        GL.glDeleteShader(shaderId)
    GL.glDeleteProgram(progId)
    raise Exception(error)

def fEsfera(u,v):
    theta = (u*math.pi)-math.pi/2
    phi = v*2*math.pi
    r = 2
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def fTroncoCone(u,v):
    theta = v*2*math.pi
    r1 = 4
    r2 = 2
    h = 2
    px = ((1-u)*(r1-r2))+r2
    x = px*math.cos(theta)
    y = u*h
    z = px*math.sin(theta)
    return x, y, z

f = fTroncoCone

def fc(u,v):
    r = u
    g = v
    b = 1-u
    return r, g, b

def indiceMalha(M=4,N=4):
    indices = array('H')
    for i in range(N-1):
        if i != 0:
            indices.append(i*M)
        for j in range(M):
            indices.append(i*M+j)
            indices.append((i+1)*M+j)
        indices.append((i+1)*M+M-1)
    return indices

def posicao(M=4,N=4):
    posicao = array('f')
    for i in range(N):
        v = i/(N-1)
        for j in range(M):
            u = j/(M-1)
            x, y, z = f(u,v)
            posicao.append(x)
            posicao.append(y)
            posicao.append(z)
    return posicao

def cor(M=4,N=4):
    cor = array('f')
    for i in range(N):
        v = i/(N-1)
        for j in range(M):
            u = j/(M-1)
            x, y, z = fc(u,v)
            cor.append(x)
            cor.append(y)
            cor.append(z)
    return cor

tamIndice = 0

def malha(): 
    global tamIndice

    M = 50
    N = 50
    aPosicao = posicao(M,N)
    aCor = cor(M,N)
    aIndices = indiceMalha(M,N)

    tamIndice = len(aIndices)
    VAO = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(VAO)
    GL.glEnableVertexAttribArray(0) # Atributo da posicao
    GL.glEnableVertexAttribArray(1) # Atributo da cor

    VBO_posicao = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_posicao)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(aPosicao)*aPosicao.itemsize, ctypes.c_void_p(aPosicao.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

    VBO_cor = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_cor)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(aCor)*aCor.itemsize, ctypes.c_void_p(aCor.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(1,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

    VBO_indice = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, VBO_indice)
    GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(aIndices)*aIndices.itemsize, ctypes.c_void_p(aIndices.buffer_info()[0]), GL.GL_STATIC_DRAW)

    return VAO

def inicializa():
    global progId, malhaVAO
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_MULTISAMPLE)
    progId = compilaShaders()
    malhaVAO = malha()

a = 0
def desenha():
    global a
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

    projection = glm.perspective(math.pi/4,800/600,0.1,100)
    camera = glm.lookAt(glm.vec3(0,2,12),glm.vec3(0,0,0),glm.vec3(0,1,0))

    model = glm.rotate(a,glm.vec3(1,0,0))
    mvp = projection * camera * model

    GL.glBindVertexArray(malhaVAO)
    GL.glUseProgram(progId)
    GL.glUniformMatrix4fv(GL.glGetUniformLocation(progId, "mvp"),1,GL.GL_FALSE,glm.value_ptr(mvp))
    GL.glDrawElements(GL.GL_TRIANGLE_STRIP,tamIndice,GL.GL_UNSIGNED_SHORT,ctypes.c_void_p(0))

    a += 0.005


def main():
    if not glfw.init():
        return
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
    glfw.window_hint(glfw.SAMPLES, 4)
    window = glfw.create_window(800, 600, "Malha", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    inicializa()
    while not glfw.window_should_close(window):
        desenha()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
