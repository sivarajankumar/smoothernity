uniform sampler2DArray texunit00;
uniform sampler2DArray texunit01;
uniform sampler2DArray texunit10;
uniform sampler2DArray texunit11;

uniform int texlayer00;
uniform int texlayer01;
uniform int texlayer10;
uniform int texlayer11;

void main()
{
    vec2 texcoord = gl_TexCoord[0].st;
    gl_FragColor = texture2DArray(texunit00, vec3(texcoord[0], texcoord[1], texlayer00));
}
