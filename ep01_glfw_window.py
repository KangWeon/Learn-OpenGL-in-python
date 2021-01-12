import platform as pltf
from OpenGL.GL import *
import glfw
import glm

# initializing glfw library

def main():
    # initializing glfw library
    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    # Configure the OpenGL context.
    # If we are planning to use anything above 2.1 we must at least
    # request a 3.3 core context to make this work across platforms.
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
    
    # 4 MSAA is a good default with wide support
    glfw.window_hint(glfw.SAMPLES, 4)

    # creating the window
    window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

    # check if window was created
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")
    
    # Query the actual framebuffer size so we can set the right viewport later
    # -> glViewport(0, 0, framebuffer_size[0], framebuffer_size[1])
    framebuffer_size = glfw.get_framebuffer_size(window)

    # set window's position
    glfw.set_window_pos(window, 100, 100)

    # make the context current
    glfw.make_context_current(window)

    # glClearColor(0.5, 0.5, 0.5, 1.0)
    print("GL_RENDERER   = ", glGetString(GL_RENDERER).decode("utf8"))
    print("GL_VERSION    = ", glGetString(GL_VERSION).decode("utf8"))

    # the main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()
        # glClear(GL_COLOR_BUFFER_BIT)
        COLOR = glm.array(glm.vec4([glm.sin(glfw.get_time()) * 0.5 + 0.5, 
                                    glm.cos(glfw.get_time()) * 0.5 + 0.5, 0.0, 1.0]))
        glClearBufferfv(GL_COLOR, 0, COLOR.ptr)

        glfw.swap_buffers(window)

    # terminate glfw, free up allocated resources
    glfw.terminate()

if __name__ == "__main__":
    main()
