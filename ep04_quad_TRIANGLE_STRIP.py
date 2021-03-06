import platform as pltf
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glfw
import numpy as np


def main():
    vertex_src = """
    # version 330

    layout(location = 0) in vec3 a_position;
    layout(location = 1) in vec3 a_color;

    out vec3 v_color;

    void main()
    {
        gl_Position = vec4(a_position, 1.0);
        v_color = a_color;
    }
    """

    fragment_src = """
    # version 330

    in vec3 v_color;
    out vec4 out_color;

    void main()
    {
        out_color = vec4(v_color, 1.0);
    }
    """

    def window_resize(window, width, height):
        glViewport(0, 0, width, height)

    # initializing glfw library
    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    if "Windows" in pltf.platform():
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    else:
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)

    # creating the window
    window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

    # check if window was created
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")

    # set window's position
    glfw.set_window_pos(window, 100, 100)

    # set the callback function for window resize
    glfw.set_window_size_callback(window, window_resize)

    # make the context current
    glfw.make_context_current(window)

    vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                -0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
                 0.5,  0.5, 0.0, 1.0, 1.0, 1.0]

    vertices = np.array(vertices, dtype=np.float32)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)

    # the main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
        glBindVertexArray(0)
        glUseProgram(0)

        glfw.swap_buffers(window)

    # terminate glfw, free up allocated resources
    glfw.terminate()

if __name__ == "__main__":
    main()
