#version 130

in vec4 pos_in;
in vec4 col_in;
smooth out vec4 col_out;

void main()
{
    col_out = col_in;
    gl_Position = pos_in;
}
