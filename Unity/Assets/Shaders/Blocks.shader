// Shader created with Shader Forge v1.21 
// Shader Forge (c) Neat Corporation / Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.21;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,lico:1,lgpr:1,limd:1,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:0,bdst:1,dpts:2,wrdp:True,dith:0,rfrpo:True,rfrpn:Refraction,coma:15,ufog:True,aust:True,igpj:False,qofs:0,qpre:1,rntp:1,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:1,x:33912,y:32700,varname:node_1,prsc:2|normal-43-RGB,emission-100-OUT;n:type:ShaderForge.SFN_Tex2d,id:2,x:33141,y:32791,ptovrint:False,ptlb:Emit Map,ptin:_EmitMap,varname:node_2892,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:fea5724c6050dc249be20446ba456d42,ntxv:3,isnm:False;n:type:ShaderForge.SFN_Tex2d,id:43,x:33400,y:32652,ptovrint:False,ptlb:Normal,ptin:_Normal,varname:node_4177,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:ff2741e3237de83498f28f6e738af8fb,ntxv:3,isnm:True;n:type:ShaderForge.SFN_Color,id:61,x:32937,y:33121,ptovrint:False,ptlb:node_61,ptin:_node_61,varname:node_7481,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:0,c2:0,c3:0,c4:1;n:type:ShaderForge.SFN_Color,id:93,x:32937,y:32947,ptovrint:False,ptlb:node_93,ptin:_node_93,varname:node_8229,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:1,c3:1,c4:1;n:type:ShaderForge.SFN_Lerp,id:94,x:33141,y:32947,varname:node_94,prsc:2|A-93-RGB,B-61-RGB,T-99-Y;n:type:ShaderForge.SFN_FragmentPosition,id:99,x:32938,y:33315,varname:node_99,prsc:2;n:type:ShaderForge.SFN_Multiply,id:100,x:33400,y:32830,varname:node_100,prsc:2|A-2-RGB,B-94-OUT;n:type:ShaderForge.SFN_Color,id:105,x:33141,y:33121,ptovrint:False,ptlb:node_105,ptin:_node_105,varname:node_7124,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:1,c3:1,c4:1;proporder:2-43-61-93-105;pass:END;sub:END;*/

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
            Name "FORWARD"
            Tags {
                "LightMode"="ForwardBase"
            }
            
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDBASE
            #include "UnityCG.cginc"
            #pragma multi_compile_fwdbase_fullshadows
            #pragma multi_compile_fog
            #pragma exclude_renderers xbox360 ps3 
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
                float3 bitangentDir : TEXCOORD4;
                UNITY_FOG_COORDS(5)
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o = (VertexOutput)0;
                o.uv0 = v.texcoord0;
                o.normalDir = UnityObjectToWorldNormal(v.normal);
                o.tangentDir = normalize( mul( _Object2World, float4( v.tangent.xyz, 0.0 ) ).xyz );
                o.bitangentDir = normalize(cross(o.normalDir, o.tangentDir) * v.tangent.w);
                o.posWorld = mul(_Object2World, v.vertex);
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                UNITY_TRANSFER_FOG(o,o.pos);
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
                i.normalDir = normalize(i.normalDir);
                float3x3 tangentTransform = float3x3( i.tangentDir, i.bitangentDir, i.normalDir);
/////// Vectors:
                float3 _Normal_var = UnpackNormal(tex2D(_Normal,TRANSFORM_TEX(i.uv0, _Normal)));
                float3 normalLocal = _Normal_var.rgb;
                float3 normalDirection = normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
////// Lighting:
////// Emissive:
                float4 _EmitMap_var = tex2D(_EmitMap,TRANSFORM_TEX(i.uv0, _EmitMap));
                float3 emissive = (_EmitMap_var.rgb*lerp(_node_93.rgb,_node_61.rgb,i.posWorld.g));
                float3 finalColor = emissive;
                fixed4 finalRGBA = fixed4(finalColor,1);
                UNITY_APPLY_FOG(i.fogCoord, finalRGBA);
                return finalRGBA;
            }
            ENDCG
        }
    }
    FallBack "Diffuse"
    CustomEditor "ShaderForgeMaterialInspector"
}
