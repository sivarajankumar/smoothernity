uniform sampler2DArray texunit;
uniform vec4 texlayer;
void main()
{
    vec2 st = gl_TexCoord[0].st;
    gl_FragColor = texture2DArray(texunit, vec3(st[0], st[1], texlayer[0]));
}
