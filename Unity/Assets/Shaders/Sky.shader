// Shader created with Shader Forge v1.21 
// Shader Forge (c) Neat Corporation / Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.21;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,lico:0,lgpr:1,limd:0,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:0,bdst:0,dpts:2,wrdp:False,dith:0,rfrpo:True,rfrpn:Refraction,coma:15,ufog:False,aust:False,igpj:True,qofs:0,qpre:0,rntp:1,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:3554,x:32690,y:33239,varname:node_3554,prsc:2|custl-3105-OUT,voffset-3105-OUT;n:type:ShaderForge.SFN_Noise,id:8580,x:31909,y:33490,varname:node_8580,prsc:2|XY-9642-UVOUT;n:type:ShaderForge.SFN_TexCoord,id:9642,x:31724,y:33490,varname:node_9642,prsc:2,uv:0;n:type:ShaderForge.SFN_Exp,id:5330,x:31969,y:32998,varname:node_5330,prsc:2,et:0;n:type:ShaderForge.SFN_Tex2d,id:3764,x:32092,y:33631,ptovrint:False,ptlb:node_3764,ptin:_node_3764,varname:node_3764,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:c82f32924341afd479ee7b1da50f853b,ntxv:2,isnm:False|UVIN-2998-OUT;n:type:ShaderForge.SFN_Add,id:3105,x:32291,y:33485,varname:node_3105,prsc:2|A-8580-OUT,B-3764-RGB;n:type:ShaderForge.SFN_Multiply,id:2998,x:31909,y:33631,varname:node_2998,prsc:2|A-9642-UVOUT,B-2543-OUT;n:type:ShaderForge.SFN_ValueProperty,id:2543,x:31724,y:33665,ptovrint:False,ptlb:node_2543,ptin:_node_2543,varname:node_2543,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:4;n:type:ShaderForge.SFN_Tex2d,id:7993,x:32244,y:33261,ptovrint:False,ptlb:node_7993,ptin:_node_7993,varname:node_7993,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,ntxv:0,isnm:False;proporder:3764-2543;pass:END;sub:END;*/

Shader "Shader Forge/Sky" {
    Properties {
        _node_3764 ("node_3764", 2D) = "black" {}
        _node_2543 ("node_2543", Float ) = 4
    }
    SubShader {
        Tags {
            "IgnoreProjector"="True"
            "Queue"="Background"
            "RenderType"="Opaque"
        }
        Pass {
            Name "FORWARD"
            Tags {
                "LightMode"="ForwardBase"
            }
            Blend One One
            ZWrite Off
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDBASE
            #include "UnityCG.cginc"
            #pragma multi_compile_fwdbase
            #pragma exclude_renderers gles3 metal d3d11_9x xbox360 xboxone ps3 ps4 psp2 
            #pragma target 3.0
            #pragma glsl
            uniform sampler2D _node_3764; uniform float4 _node_3764_ST;
            uniform float _node_2543;
            struct VertexInput {
                float4 vertex : POSITION;
                float2 texcoord0 : TEXCOORD0;
            };
            struct VertexOutput {
                float4 pos : SV_POSITION;
                float2 uv0 : TEXCOORD0;
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o = (VertexOutput)0;
                o.uv0 = v.texcoord0;
                float2 node_8580_skew = o.uv0 + 0.2127+o.uv0.x*0.3713*o.uv0.y;
                float2 node_8580_rnd = 4.789*sin(489.123*(node_8580_skew));
                float node_8580 = frac(node_8580_rnd.x*node_8580_rnd.y*(1+node_8580_skew.x));
                float2 node_2998 = (o.uv0*_node_2543);
                float4 _node_3764_var = tex2Dlod(_node_3764,float4(TRANSFORM_TEX(node_2998, _node_3764),0.0,0));
                float3 node_3105 = (node_8580+_node_3764_var.rgb);
                v.vertex.xyz += node_3105;
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
/////// Vectors:
////// Lighting:
                float2 node_8580_skew = i.uv0 + 0.2127+i.uv0.x*0.3713*i.uv0.y;
                float2 node_8580_rnd = 4.789*sin(489.123*(node_8580_skew));
                float node_8580 = frac(node_8580_rnd.x*node_8580_rnd.y*(1+node_8580_skew.x));
                float2 node_2998 = (i.uv0*_node_2543);
                float4 _node_3764_var = tex2D(_node_3764,TRANSFORM_TEX(node_2998, _node_3764));
                float3 node_3105 = (node_8580+_node_3764_var.rgb);
                float3 finalColor = node_3105;
                return fixed4(finalColor,1);
            }
            ENDCG
        }
        Pass {
            Name "ShadowCaster"
            Tags {
                "LightMode"="ShadowCaster"
            }
            Offset 1, 1
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_SHADOWCASTER
            #include "UnityCG.cginc"
            #include "Lighting.cginc"
            #pragma fragmentoption ARB_precision_hint_fastest
            #pragma multi_compile_shadowcaster
            #pragma exclude_renderers gles3 metal d3d11_9x xbox360 xboxone ps3 ps4 psp2 
            #pragma target 3.0
            #pragma glsl
            uniform sampler2D _node_3764; uniform float4 _node_3764_ST;
            uniform float _node_2543;
            struct VertexInput {
                float4 vertex : POSITION;
                float2 texcoord0 : TEXCOORD0;
            };
            struct VertexOutput {
                V2F_SHADOW_CASTER;
                float2 uv0 : TEXCOORD1;
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o = (VertexOutput)0;
                o.uv0 = v.texcoord0;
                float2 node_8580_skew = o.uv0 + 0.2127+o.uv0.x*0.3713*o.uv0.y;
                float2 node_8580_rnd = 4.789*sin(489.123*(node_8580_skew));
                float node_8580 = frac(node_8580_rnd.x*node_8580_rnd.y*(1+node_8580_skew.x));
                float2 node_2998 = (o.uv0*_node_2543);
                float4 _node_3764_var = tex2Dlod(_node_3764,float4(TRANSFORM_TEX(node_2998, _node_3764),0.0,0));
                float3 node_3105 = (node_8580+_node_3764_var.rgb);
                v.vertex.xyz += node_3105;
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                TRANSFER_SHADOW_CASTER(o)
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
/////// Vectors:
                SHADOW_CASTER_FRAGMENT(i)
            }
            ENDCG
        }
    }
    FallBack "Diffuse"
    CustomEditor "ShaderForgeMaterialInspector"
}
