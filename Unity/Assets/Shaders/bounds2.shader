// Shader created with Shader Forge v1.21 
// Shader Forge (c) Neat Corporation / Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.21;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,lico:1,lgpr:1,limd:1,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:3,bdst:7,dpts:2,wrdp:False,dith:0,rfrpo:True,rfrpn:Refraction,coma:15,ufog:True,aust:True,igpj:True,qofs:0,qpre:3,rntp:2,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:4013,x:33805,y:32585,varname:node_4013,prsc:2|diff-3742-OUT,normal-4188-RGB,emission-5158-RGB,lwrap-2688-OUT,alpha-3952-OUT,clip-464-OUT;n:type:ShaderForge.SFN_Tex2d,id:5379,x:32351,y:33099,ptovrint:False,ptlb:Slice Guide,ptin:_SliceGuide,varname:node_5379,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:e2c3fa6a05ef10e468875bdfc6d72375,ntxv:0,isnm:False;n:type:ShaderForge.SFN_Slider,id:1767,x:32016,y:32911,ptovrint:False,ptlb:Dissolve Amount,ptin:_DissolveAmount,varname:node_1767,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,min:0,cur:0.9230769,max:1;n:type:ShaderForge.SFN_Add,id:464,x:32513,y:32911,varname:node_464,prsc:2|A-9560-OUT,B-5379-R;n:type:ShaderForge.SFN_RemapRange,id:9560,x:32351,y:32911,varname:node_9560,prsc:2,frmn:0,frmx:1,tomn:-0.85,tomx:0.85|IN-1767-OUT;n:type:ShaderForge.SFN_RemapRange,id:8347,x:32755,y:32759,varname:node_8347,prsc:2,frmn:0,frmx:1,tomn:-2,tomx:2|IN-464-OUT;n:type:ShaderForge.SFN_Clamp01,id:4832,x:32916,y:32759,varname:node_4832,prsc:2|IN-8347-OUT;n:type:ShaderForge.SFN_Append,id:4762,x:33102,y:32702,varname:node_4762,prsc:2|A-4832-OUT,B-9819-OUT;n:type:ShaderForge.SFN_ValueProperty,id:9819,x:32916,y:32900,ptovrint:False,ptlb:node_9819,ptin:_node_9819,varname:node_9819,prsc:2,glob:False,taghide:True,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:0;n:type:ShaderForge.SFN_Tex2dAsset,id:3412,x:33102,y:32870,ptovrint:False,ptlb:Ramp,ptin:_Ramp,varname:node_3412,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:1359e7325b2c1474f90fbb517ef42bfa,ntxv:0,isnm:False;n:type:ShaderForge.SFN_Tex2d,id:5158,x:33290,y:32701,varname:node_5158,prsc:2,tex:1359e7325b2c1474f90fbb517ef42bfa,ntxv:0,isnm:False|UVIN-4762-OUT,TEX-3412-TEX;n:type:ShaderForge.SFN_Slider,id:3952,x:33102,y:33104,ptovrint:False,ptlb:Opacity,ptin:_Opacity,varname:node_3952,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,min:0,cur:0.5213675,max:1;n:type:ShaderForge.SFN_Tex2d,id:4188,x:33292,y:32542,ptovrint:False,ptlb:Normal,ptin:_Normal,varname:node_4188,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:814f992ab6934004e95fdcbd9fa83712,ntxv:3,isnm:True|UVIN-7208-OUT;n:type:ShaderForge.SFN_Tex2d,id:60,x:33292,y:32354,ptovrint:False,ptlb:Texture,ptin:_Texture,varname:node_60,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:0ab39eda1cb9ed44eba7c1d3a1a48baa,ntxv:0,isnm:False|UVIN-7208-OUT;n:type:ShaderForge.SFN_Slider,id:156,x:32047,y:32400,ptovrint:False,ptlb:Scale,ptin:_Scale,varname:node_156,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,min:0,cur:0,max:1;n:type:ShaderForge.SFN_Multiply,id:8253,x:32392,y:32401,varname:node_8253,prsc:2|A-456-OUT,B-156-OUT;n:type:ShaderForge.SFN_Add,id:9138,x:32579,y:32412,varname:node_9138,prsc:2|A-8253-OUT,B-4160-OUT;n:type:ShaderForge.SFN_Vector1,id:4160,x:32392,y:32539,varname:node_4160,prsc:2,v1:0.1;n:type:ShaderForge.SFN_ValueProperty,id:456,x:32204,y:32331,ptovrint:False,ptlb:Max Scale,ptin:_MaxScale,varname:node_456,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:32;n:type:ShaderForge.SFN_Multiply,id:7208,x:33023,y:32241,varname:node_7208,prsc:2|A-8806-OUT,B-9138-OUT;n:type:ShaderForge.SFN_Color,id:6867,x:33292,y:32190,ptovrint:False,ptlb:Color,ptin:_Color,varname:node_6867,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:0,c3:0,c4:1;n:type:ShaderForge.SFN_Multiply,id:3742,x:33519,y:32282,varname:node_3742,prsc:2|A-6867-RGB,B-60-RGB;n:type:ShaderForge.SFN_Sin,id:7182,x:33219,y:33263,varname:node_7182,prsc:2|IN-9618-OUT;n:type:ShaderForge.SFN_Time,id:8933,x:32892,y:33263,varname:node_8933,prsc:2;n:type:ShaderForge.SFN_Multiply,id:9618,x:33061,y:33263,varname:node_9618,prsc:2|A-8933-T,B-9899-OUT;n:type:ShaderForge.SFN_Vector1,id:9899,x:32892,y:33387,varname:node_9899,prsc:2,v1:55;n:type:ShaderForge.SFN_Vector1,id:7107,x:32892,y:33451,varname:node_7107,prsc:2,v1:25;n:type:ShaderForge.SFN_Multiply,id:4126,x:33061,y:33417,varname:node_4126,prsc:2|A-8933-T,B-7107-OUT;n:type:ShaderForge.SFN_Sin,id:4317,x:33219,y:33417,varname:node_4317,prsc:2|IN-4126-OUT;n:type:ShaderForge.SFN_Add,id:2688,x:33401,y:33261,varname:node_2688,prsc:2|A-7182-OUT,B-4317-OUT,C-4153-OUT;n:type:ShaderForge.SFN_Vector1,id:6997,x:32892,y:33605,varname:node_6997,prsc:2,v1:100;n:type:ShaderForge.SFN_Multiply,id:5324,x:33061,y:33571,varname:node_5324,prsc:2|A-8933-T,B-6997-OUT;n:type:ShaderForge.SFN_Sin,id:4153,x:33219,y:33571,varname:node_4153,prsc:2|IN-5324-OUT;n:type:ShaderForge.SFN_TexCoord,id:7136,x:32770,y:31708,varname:node_7136,prsc:2,uv:0;n:type:ShaderForge.SFN_Add,id:8806,x:32932,y:31849,varname:node_8806,prsc:2|A-7136-UVOUT,B-6717-OUT;n:type:ShaderForge.SFN_Append,id:6880,x:34262,y:32224,varname:node_6880,prsc:2;n:type:ShaderForge.SFN_Time,id:3396,x:32546,y:31977,varname:node_3396,prsc:2;n:type:ShaderForge.SFN_Multiply,id:6717,x:32763,y:31996,varname:node_6717,prsc:2|A-3396-T,B-9921-OUT;n:type:ShaderForge.SFN_Vector1,id:9921,x:32730,y:32202,varname:node_9921,prsc:2,v1:0.2;proporder:5379-1767-9819-3412-3952-4188-60-156-456-6867;pass:END;sub:END;*/

Shader "Shader Forge/bounds2" {
    Properties {
        _SliceGuide ("Slice Guide", 2D) = "white" {}
        _DissolveAmount ("Dissolve Amount", Range(0, 1)) = 0.9230769
        [HideInInspector]_node_9819 ("node_9819", Float ) = 0
        _Ramp ("Ramp", 2D) = "white" {}
        _Opacity ("Opacity", Range(0, 1)) = 0.5213675
        _Normal ("Normal", 2D) = "bump" {}
        _Texture ("Texture", 2D) = "white" {}
        _Scale ("Scale", Range(0, 1)) = 0
        _MaxScale ("Max Scale", Float ) = 32
        _Color ("Color", Color) = (1,0,0,1)
        [HideInInspector]_Cutoff ("Alpha cutoff", Range(0,1)) = 0.5
    }
    SubShader {
        Tags {
            "IgnoreProjector"="True"
            "Queue"="Transparent"
            "RenderType"="Transparent"
        }
        Pass {
            Name "FORWARD"
            Tags {
                "LightMode"="ForwardBase"
            }
            Blend SrcAlpha OneMinusSrcAlpha
            ZWrite Off
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDBASE
            #include "UnityCG.cginc"
            #pragma multi_compile_fwdbase
            #pragma multi_compile_fog
            #pragma exclude_renderers gles3 metal d3d11_9x xbox360 xboxone ps3 ps4 psp2 
            #pragma target 3.0
            uniform float4 _LightColor0;
            uniform float4 _TimeEditor;
            uniform sampler2D _SliceGuide; uniform float4 _SliceGuide_ST;
            uniform float _DissolveAmount;
            uniform float _node_9819;
            uniform sampler2D _Ramp; uniform float4 _Ramp_ST;
            uniform float _Opacity;
            uniform sampler2D _Normal; uniform float4 _Normal_ST;
            uniform sampler2D _Texture; uniform float4 _Texture_ST;
            uniform float _Scale;
            uniform float _MaxScale;
            uniform float4 _Color;
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
                float3 lightColor = _LightColor0.rgb;
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                UNITY_TRANSFER_FOG(o,o.pos);
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
                i.normalDir = normalize(i.normalDir);
                float3x3 tangentTransform = float3x3( i.tangentDir, i.bitangentDir, i.normalDir);
/////// Vectors:
                float3 viewDirection = normalize(_WorldSpaceCameraPos.xyz - i.posWorld.xyz);
                float4 node_3396 = _Time + _TimeEditor;
                float2 node_7208 = ((i.uv0+(node_3396.g*0.2))*((_MaxScale*_Scale)+0.1));
                float3 _Normal_var = UnpackNormal(tex2D(_Normal,TRANSFORM_TEX(node_7208, _Normal)));
                float3 normalLocal = _Normal_var.rgb;
                float3 normalDirection = normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
                float4 _SliceGuide_var = tex2D(_SliceGuide,TRANSFORM_TEX(i.uv0, _SliceGuide));
                float node_464 = ((_DissolveAmount*1.7+-0.85)+_SliceGuide_var.r);
                clip(node_464 - 0.5);
                float3 lightDirection = normalize(_WorldSpaceLightPos0.xyz);
                float3 lightColor = _LightColor0.rgb;
////// Lighting:
                float attenuation = 1;
                float3 attenColor = attenuation * _LightColor0.xyz;
/////// Diffuse:
                float NdotL = dot( normalDirection, lightDirection );
                float4 node_8933 = _Time + _TimeEditor;
                float node_2688 = (sin((node_8933.g*55.0))+sin((node_8933.g*25.0))+sin((node_8933.g*100.0)));
                float3 w = float3(node_2688,node_2688,node_2688)*0.5; // Light wrapping
                float3 NdotLWrap = NdotL * ( 1.0 - w );
                float3 forwardLight = max(float3(0.0,0.0,0.0), NdotLWrap + w );
                NdotL = max(0.0,dot( normalDirection, lightDirection ));
                float3 directDiffuse = forwardLight * attenColor;
                float3 indirectDiffuse = float3(0,0,0);
                indirectDiffuse += UNITY_LIGHTMODEL_AMBIENT.rgb; // Ambient Light
                float4 _Texture_var = tex2D(_Texture,TRANSFORM_TEX(node_7208, _Texture));
                float3 diffuseColor = (_Color.rgb*_Texture_var.rgb);
                float3 diffuse = (directDiffuse + indirectDiffuse) * diffuseColor;
////// Emissive:
                float2 node_4762 = float2(saturate((node_464*4.0+-2.0)),_node_9819);
                float4 node_5158 = tex2D(_Ramp,TRANSFORM_TEX(node_4762, _Ramp));
                float3 emissive = node_5158.rgb;
/// Final Color:
                float3 finalColor = diffuse + emissive;
                fixed4 finalRGBA = fixed4(finalColor,_Opacity);
                UNITY_APPLY_FOG(i.fogCoord, finalRGBA);
                return finalRGBA;
            }
            ENDCG
        }
        Pass {
            Name "FORWARD_DELTA"
            Tags {
                "LightMode"="ForwardAdd"
            }
            Blend One One
            ZWrite Off
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDADD
            #include "UnityCG.cginc"
            #include "AutoLight.cginc"
            #pragma multi_compile_fwdadd
            #pragma multi_compile_fog
            #pragma exclude_renderers gles3 metal d3d11_9x xbox360 xboxone ps3 ps4 psp2 
            #pragma target 3.0
            uniform float4 _LightColor0;
            uniform float4 _TimeEditor;
            uniform sampler2D _SliceGuide; uniform float4 _SliceGuide_ST;
            uniform float _DissolveAmount;
            uniform float _node_9819;
            uniform sampler2D _Ramp; uniform float4 _Ramp_ST;
            uniform float _Opacity;
            uniform sampler2D _Normal; uniform float4 _Normal_ST;
            uniform sampler2D _Texture; uniform float4 _Texture_ST;
            uniform float _Scale;
            uniform float _MaxScale;
            uniform float4 _Color;
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
                LIGHTING_COORDS(5,6)
                UNITY_FOG_COORDS(7)
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o = (VertexOutput)0;
                o.uv0 = v.texcoord0;
                o.normalDir = UnityObjectToWorldNormal(v.normal);
                o.tangentDir = normalize( mul( _Object2World, float4( v.tangent.xyz, 0.0 ) ).xyz );
                o.bitangentDir = normalize(cross(o.normalDir, o.tangentDir) * v.tangent.w);
                o.posWorld = mul(_Object2World, v.vertex);
                float3 lightColor = _LightColor0.rgb;
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                UNITY_TRANSFER_FOG(o,o.pos);
                TRANSFER_VERTEX_TO_FRAGMENT(o)
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
                i.normalDir = normalize(i.normalDir);
                float3x3 tangentTransform = float3x3( i.tangentDir, i.bitangentDir, i.normalDir);
/////// Vectors:
                float3 viewDirection = normalize(_WorldSpaceCameraPos.xyz - i.posWorld.xyz);
                float4 node_3396 = _Time + _TimeEditor;
                float2 node_7208 = ((i.uv0+(node_3396.g*0.2))*((_MaxScale*_Scale)+0.1));
                float3 _Normal_var = UnpackNormal(tex2D(_Normal,TRANSFORM_TEX(node_7208, _Normal)));
                float3 normalLocal = _Normal_var.rgb;
                float3 normalDirection = normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
                float4 _SliceGuide_var = tex2D(_SliceGuide,TRANSFORM_TEX(i.uv0, _SliceGuide));
                float node_464 = ((_DissolveAmount*1.7+-0.85)+_SliceGuide_var.r);
                clip(node_464 - 0.5);
                float3 lightDirection = normalize(lerp(_WorldSpaceLightPos0.xyz, _WorldSpaceLightPos0.xyz - i.posWorld.xyz,_WorldSpaceLightPos0.w));
                float3 lightColor = _LightColor0.rgb;
////// Lighting:
                float attenuation = LIGHT_ATTENUATION(i);
                float3 attenColor = attenuation * _LightColor0.xyz;
/////// Diffuse:
                float NdotL = dot( normalDirection, lightDirection );
                float4 node_8933 = _Time + _TimeEditor;
                float node_2688 = (sin((node_8933.g*55.0))+sin((node_8933.g*25.0))+sin((node_8933.g*100.0)));
                float3 w = float3(node_2688,node_2688,node_2688)*0.5; // Light wrapping
                float3 NdotLWrap = NdotL * ( 1.0 - w );
                float3 forwardLight = max(float3(0.0,0.0,0.0), NdotLWrap + w );
                NdotL = max(0.0,dot( normalDirection, lightDirection ));
                float3 directDiffuse = forwardLight * attenColor;
                float4 _Texture_var = tex2D(_Texture,TRANSFORM_TEX(node_7208, _Texture));
                float3 diffuseColor = (_Color.rgb*_Texture_var.rgb);
                float3 diffuse = directDiffuse * diffuseColor;
/// Final Color:
                float3 finalColor = diffuse;
                fixed4 finalRGBA = fixed4(finalColor * _Opacity,0);
                UNITY_APPLY_FOG(i.fogCoord, finalRGBA);
                return finalRGBA;
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
            #pragma multi_compile_fog
            #pragma exclude_renderers gles3 metal d3d11_9x xbox360 xboxone ps3 ps4 psp2 
            #pragma target 3.0
            uniform sampler2D _SliceGuide; uniform float4 _SliceGuide_ST;
            uniform float _DissolveAmount;
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
                o.pos = mul(UNITY_MATRIX_MVP, v.vertex );
                TRANSFER_SHADOW_CASTER(o)
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
/////// Vectors:
                float4 _SliceGuide_var = tex2D(_SliceGuide,TRANSFORM_TEX(i.uv0, _SliceGuide));
                float node_464 = ((_DissolveAmount*1.7+-0.85)+_SliceGuide_var.r);
                clip(node_464 - 0.5);
                SHADOW_CASTER_FRAGMENT(i)
            }
            ENDCG
        }
    }
    FallBack "Diffuse"
    CustomEditor "ShaderForgeMaterialInspector"
}
