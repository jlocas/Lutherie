// Shader created with Shader Forge Beta 0.36 
// Shader Forge (c) Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:0.36;sub:START;pass:START;ps:flbk:,lico:1,lgpr:1,nrmq:1,limd:1,uamb:True,mssp:True,lmpd:False,lprd:False,enco:False,frtr:True,vitr:True,dbil:False,rmgx:True,rpth:0,hqsc:True,hqlp:False,tesm:0,blpr:0,bsrc:0,bdst:0,culm:0,dpts:2,wrdp:True,ufog:True,aust:True,igpj:False,qofs:0,qpre:1,rntp:1,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:1,x:32460,y:32700|normal-43-RGB,emission-100-OUT;n:type:ShaderForge.SFN_Tex2d,id:2,x:33300,y:32791,ptlb:Emit Map,ptin:_EmitMap,tex:fea5724c6050dc249be20446ba456d42,ntxv:3,isnm:False;n:type:ShaderForge.SFN_Tex2d,id:43,x:33041,y:32652,ptlb:Normal,ptin:_Normal,tex:ff2741e3237de83498f28f6e738af8fb,ntxv:3,isnm:True;n:type:ShaderForge.SFN_Color,id:61,x:33504,y:33121,ptlb:node_61,ptin:_node_61,glob:False,c1:0,c2:0,c3:0,c4:1;n:type:ShaderForge.SFN_Color,id:93,x:33504,y:32947,ptlb:node_93,ptin:_node_93,glob:False,c1:1,c2:1,c3:1,c4:1;n:type:ShaderForge.SFN_Lerp,id:94,x:33300,y:32947|A-93-RGB,B-61-RGB,T-99-Y;n:type:ShaderForge.SFN_FragmentPosition,id:99,x:33503,y:33315;n:type:ShaderForge.SFN_Multiply,id:100,x:33041,y:32830|A-2-RGB,B-94-OUT;n:type:ShaderForge.SFN_Color,id:105,x:33300,y:33121,ptlb:node_105,ptin:_node_105,glob:False,c1:1,c2:1,c3:1,c4:1;proporder:2-43-61-93-105;pass:END;sub:END;*/

Shader "Shader Forge/Blocks" {
    Properties {
        _EmitMap ("Emit Map", 2D) = "bump" {}
        _Normal ("Normal", 2D) = "bump" {}
        _node_61 ("node_61", Color) = (0,0,0,1)
        _node_93 ("node_93", Color) = (1,1,1,1)
        _node_105 ("node_105", Color) = (1,1,1,1)
    }
    SubShader {
        Tags {
            "RenderType"="Opaque"
        }
        Pass {
            Name "ForwardBase"
            Tags {
                "LightMode"="ForwardBase"
            }
            
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDBASE
            #include "UnityCG.cginc"
            #pragma multi_compile_fwdbase_fullshadows
            #pragma exclude_renderers xbox360 ps3 flash d3d11_9x 
            #pragma target 3.0
            uniform sampler2D _EmitMap; uniform float4 _EmitMap_ST;
            uniform sampler2D _Normal; uniform float4 _Normal_ST;
            uniform float4 _node_61;
            uniform float4 _node_93;
            struct VertexInput {
                float4 vertex : POSITION;
                float3 normal : NORMAL;
                float4 tangent : TANGENT;
                float2 texcoord0 : TEXCOORD0;
            };
            struct VertexOutput {
                float4 pos : SV_POSITION;
                float2 uv0 : TEXCOORD0;
                float4 posWorld : TEXCOORD1;
                float3 normalDir : TEXCOORD2;
                float3 tangentDir : TEXCOORD3;
                float3 binormalDir : TEXCOORD4;
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o;
                o.uv0 = v.texcoord0;
                o.normalDir = mul(float4(v.normal,0), _World2Object).xyz;
                o.tangentDir = normalize( mul( _Object2World, float4( v.tangent.xyz, 0.0 ) ).xyz );
                o.binormalDir = normalize(cross(o.normalDir, o.tangentDir) * v.tangent.w);
                o.posWorld = mul(_Object2World, v.vertex);
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex);
                return o;
            }
            fixed4 frag(VertexOutput i) : COLOR {
                i.normalDir = normalize(i.normalDir);
                float3x3 tangentTransform = float3x3( i.tangentDir, i.binormalDir, i.normalDir);
/////// Normals:
                float2 node_113 = i.uv0;
                float3 normalLocal = UnpackNormal(tex2D(_Normal,TRANSFORM_TEX(node_113.rg, _Normal))).rgb;
                float3 normalDirection =  normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
////// Lighting:
////// Emissive:
                float3 emissive = (tex2D(_EmitMap,TRANSFORM_TEX(node_113.rg, _EmitMap)).rgb*lerp(_node_93.rgb,_node_61.rgb,i.posWorld.g));
                float3 finalColor = emissive;
/// Final Color:
                return fixed4(finalColor,1);
            }
            ENDCG
        }
    }
    FallBack "Diffuse"
    CustomEditor "ShaderForgeMaterialInspector"
}
