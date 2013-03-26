uniform sampler2DArray texunit00;
uniform sampler2DArray texunit01;
uniform sampler2DArray texunit10;
uniform sampler2DArray texunit11;

uniform int texlayer00;
uniform int texlayer01;
uniform int texlayer10;
uniform int texlayer11;

const float OVERLAP = 0.3;

void main()
{
    vec2 texcoord = gl_TexCoord[0].st;
    vec4 color00 = texture2DArray(texunit00, vec3(texcoord[0], texcoord[1], texlayer00));
    vec4 color01 = texture2DArray(texunit01, vec3(texcoord[0], texcoord[1] + 1, texlayer01));
    vec4 color10 = texture2DArray(texunit10, vec3(texcoord[0] + 1, texcoord[1], texlayer10));
    vec4 color11 = texture2DArray(texunit11, vec3(texcoord[0] + 1, texcoord[1] + 1, texlayer11));
    vec2 weight = vec2(smoothstep(0, OVERLAP, texcoord[0]),
                       smoothstep(0, OVERLAP, texcoord[1]));
    vec4 colorx0 = color00*weight[0] + color10*(1.0 - weight[0]);
    vec4 colorx1 = color01*weight[0] + color11*(1.0 - weight[0]);
    vec4 colorz  = colorx0*weight[1] + colorx1*(1.0 - weight[1]);
    gl_FragColor = colorz;
}
