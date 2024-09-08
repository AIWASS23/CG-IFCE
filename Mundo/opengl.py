from OpenGL.GL import *
import OpenGL.GL as gl

def print_opengl_functions():
    print("GL_VERSION:", gl.glGetString(GL_VERSION))
    print("GL_VENDOR:", gl.glGetString(GL_VENDOR))
    print("GL_RENDERER:", gl.glGetString(GL_RENDERER))
    print("GL_SHADING_LANGUAGE_VERSION:", gl.glGetString(GL_SHADING_LANGUAGE_VERSION))
    print("Available Functions:")
    for function in dir(gl):
        if function.startswith("gl"):
            print(function)

print_opengl_functions()
