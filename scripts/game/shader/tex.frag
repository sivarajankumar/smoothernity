uniform sampler2DArray texunit;
uniform vec4 texlayer;
void main()
{
    vec2 texcoord = gl_TexCoord[0].st;
    gl_FragColor = texture2DArray(texunit, vec3(texcoord[0], texcoord[1], texlayer[0]));
}
