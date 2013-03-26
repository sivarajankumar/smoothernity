in vec3 position;
in vec2 texCoord;
in vec4 color;

void main()
{
    gl_Position = ftransform();
}
