// Shader created with Shader Forge v1.21 
// Shader Forge (c) Neat Corporation / Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.21;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,lico:1,lgpr:1,limd:1,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:0,bdst:1,dpts:2,wrdp:True,dith:0,rfrpo:True,rfrpn:Refraction,coma:15,ufog:True,aust:True,igpj:False,qofs:0,qpre:1,rntp:1,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:1,x:34817,y:32664,varname:node_1,prsc:2|diff-8546-OUT,spec-9318-OUT,gloss-1673-OUT,normal-5954-RGB,emission-1482-OUT;n:type:ShaderForge.SFN_Tex2d,id:9026,x:33305,y:32224,ptovrint:False,ptlb:Texture,ptin:_Texture,varname:node_9026,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:fea5724c6050dc249be20446ba456d42,ntxv:0,isnm:False|UVIN-3062-UVOUT;n:type:ShaderForge.SFN_TexCoord,id:3062,x:33124,y:32224,varname:node_3062,prsc:2,uv:0;n:type:ShaderForge.SFN_Tex2d,id:5954,x:33305,y:32423,ptovrint:False,ptlb:Normal Map,ptin:_NormalMap,varname:_Texture_copy,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:ff2741e3237de83498f28f6e738af8fb,ntxv:3,isnm:True|UVIN-3062-UVOUT;n:type:ShaderForge.SFN_Multiply,id:5121,x:33706,y:32224,varname:node_5121,prsc:2|A-6117-OUT,B-4751-OUT;n:type:ShaderForge.SFN_Vector1,id:4751,x:33552,y:32258,varname:node_4751,prsc:2,v1:-1;n:type:ShaderForge.SFN_Add,id:9318,x:33999,y:32224,varname:node_9318,prsc:2|A-5121-OUT,B-5097-OUT;n:type:ShaderForge.SFN_Vector1,id:5097,x:33843,y:32258,varname:node_5097,prsc:2,v1:1;n:type:ShaderForge.SFN_Relay,id:6117,x:33496,y:32224,varname:node_6117,prsc:2|IN-9026-RGB;n:type:ShaderForge.SFN_ValueProperty,id:1673,x:34328,y:32617,ptovrint:False,ptlb:Gloss,ptin:_Gloss,varname:node_1673,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1.3;n:type:ShaderForge.SFN_Multiply,id:8546,x:33634,y:32811,varname:node_8546,prsc:2|A-9026-RGB,B-2466-RGB;n:type:ShaderForge.SFN_ValueProperty,id:532,x:33526,y:33624,ptovrint:False,ptlb:Max Emit Height,ptin:_MaxEmitHeight,varname:node_532,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:5;n:type:ShaderForge.SFN_Divide,id:2052,x:33701,y:33590,varname:node_2052,prsc:2|A-3631-OUT,B-8810-OUT;n:type:ShaderForge.SFN_Clamp01,id:9803,x:33863,y:33590,varname:node_9803,prsc:2|IN-2052-OUT;n:type:ShaderForge.SFN_Lerp,id:434,x:34241,y:33473,varname:node_434,prsc:2|A-4524-OUT,B-5573-OUT,T-2115-OUT;n:type:ShaderForge.SFN_Vector1,id:4524,x:34010,y:33473,varname:node_4524,prsc:2,v1:0;n:type:ShaderForge.SFN_Abs,id:3631,x:33701,y:33442,varname:node_3631,prsc:2|IN-6226-Y;n:type:ShaderForge.SFN_FragmentPosition,id:6226,x:33526,y:33442,varname:node_6226,prsc:2;n:type:ShaderForge.SFN_ValueProperty,id:5331,x:33863,y:33745,ptovrint:False,ptlb:Emit Mul,ptin:_EmitMul,varname:node_5331,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1;n:type:ShaderForge.SFN_Multiply,id:2115,x:34041,y:33590,varname:node_2115,prsc:2|A-9803-OUT,B-5331-OUT;n:type:ShaderForge.SFN_Relay,id:5573,x:34010,y:33531,varname:node_5573,prsc:2|IN-8546-OUT;n:type:ShaderForge.SFN_Tex2d,id:2466,x:33144,y:33198,varname:node_2466,prsc:2,tex:cfdd1e32fa245924db8437d5f6042924,ntxv:0,isnm:False|UVIN-1056-OUT,TEX-1062-TEX;n:type:ShaderForge.SFN_Tex2dAsset,id:1062,x:32911,y:33217,ptovrint:False,ptlb:Ramp,ptin:_Ramp,varname:node_1062,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:cfdd1e32fa245924db8437d5f6042924,ntxv:0,isnm:False;n:type:ShaderForge.SFN_ValueProperty,id:8810,x:32195,y:33064,ptovrint:False,ptlb:Max Height,ptin:_MaxHeight,varname:node_8810,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:5;n:type:ShaderForge.SFN_RemapRangeAdvanced,id:8144,x:32572,y:33064,varname:node_8144,prsc:2|IN-5124-Y,IMIN-6123-OUT,IMAX-8810-OUT,OMIN-6355-OUT,OMAX-5156-OUT;n:type:ShaderForge.SFN_Vector1,id:6355,x:32372,y:33205,varname:node_6355,prsc:2,v1:0;n:type:ShaderForge.SFN_Vector1,id:5156,x:32372,y:33258,varname:node_5156,prsc:2,v1:1;n:type:ShaderForge.SFN_Negate,id:6123,x:32372,y:33064,varname:node_6123,prsc:2|IN-8810-OUT;n:type:ShaderForge.SFN_FragmentPosition,id:5124,x:32195,y:32914,varname:node_5124,prsc:2;n:type:ShaderForge.SFN_Clamp01,id:7013,x:32737,y:33064,varname:node_7013,prsc:2|IN-8144-OUT;n:type:ShaderForge.SFN_Append,id:1056,x:32911,y:33064,varname:node_1056,prsc:2|A-7013-OUT,B-2680-OUT;n:type:ShaderForge.SFN_Vector1,id:2680,x:32737,y:33181,varname:node_2680,prsc:2,v1:0;n:type:ShaderForge.SFN_ValueProperty,id:1277,x:34241,y:33624,ptovrint:False,ptlb:Emit Min,ptin:_EmitMin,varname:_EmitMul_copy,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1;n:type:ShaderForge.SFN_Add,id:1482,x:34416,y:33473,varname:node_1482,prsc:2|A-434-OUT,B-1277-OUT;proporder:9026-5954-1673-532-5331-1062-8810-1277;pass:END;sub:END;*/

Shader "Shader Forge/Blocks" {
    Properties {
        _Texture ("Texture", 2D) = "white" {}
        _NormalMap ("Normal Map", 2D) = "bump" {}
        _Gloss ("Gloss", Float ) = 1.3
        _MaxEmitHeight ("Max Emit Height", Float ) = 5
        _EmitMul ("Emit Mul", Float ) = 1
        _Ramp ("Ramp", 2D) = "white" {}
        _MaxHeight ("Max Height", Float ) = 5
        _EmitMin ("Emit Min", Float ) = 1
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
            #include "AutoLight.cginc"
            #pragma multi_compile_fwdbase_fullshadows
            #pragma multi_compile_fog
            #pragma exclude_renderers xbox360 ps3 
            #pragma target 3.0
            uniform float4 _LightColor0;
            uniform sampler2D _Texture; uniform float4 _Texture_ST;
            uniform sampler2D _NormalMap; uniform float4 _NormalMap_ST;
            uniform float _Gloss;
            uniform float _EmitMul;
            uniform sampler2D _Ramp; uniform float4 _Ramp_ST;
            uniform float _MaxHeight;
            uniform float _EmitMin;
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
                float3 _NormalMap_var = UnpackNormal(tex2D(_NormalMap,TRANSFORM_TEX(i.uv0, _NormalMap)));
                float3 normalLocal = _NormalMap_var.rgb;
                float3 normalDirection = normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
                float3 lightDirection = normalize(_WorldSpaceLightPos0.xyz);
                float3 lightColor = _LightColor0.rgb;
                float3 halfDirection = normalize(viewDirection+lightDirection);
////// Lighting:
                float attenuation = LIGHT_ATTENUATION(i);
                float3 attenColor = attenuation * _LightColor0.xyz;
///////// Gloss:
                float gloss = _Gloss;
                float specPow = exp2( gloss * 10.0+1.0);
////// Specular:
                float NdotL = max(0, dot( normalDirection, lightDirection ));
                float4 _Texture_var = tex2D(_Texture,TRANSFORM_TEX(i.uv0, _Texture));
                float3 specularColor = ((_Texture_var.rgb*(-1.0))+1.0);
                float3 directSpecular = (floor(attenuation) * _LightColor0.xyz) * pow(max(0,dot(halfDirection,normalDirection)),specPow)*specularColor;
                float3 specular = directSpecular;
/////// Diffuse:
                NdotL = max(0.0,dot( normalDirection, lightDirection ));
                float3 directDiffuse = max( 0.0, NdotL) * attenColor;
                float3 indirectDiffuse = float3(0,0,0);
                indirectDiffuse += UNITY_LIGHTMODEL_AMBIENT.rgb; // Ambient Light
                float node_6123 = (-1*_MaxHeight);
                float node_6355 = 0.0;
                float2 node_1056 = float2(saturate((node_6355 + ( (i.posWorld.g - node_6123) * (1.0 - node_6355) ) / (_MaxHeight - node_6123))),0.0);
                float4 node_2466 = tex2D(_Ramp,TRANSFORM_TEX(node_1056, _Ramp));
                float3 node_8546 = (_Texture_var.rgb*node_2466.rgb);
                float3 diffuseColor = node_8546;
                float3 diffuse = (directDiffuse + indirectDiffuse) * diffuseColor;
////// Emissive:
                float node_4524 = 0.0;
                float3 emissive = (lerp(float3(node_4524,node_4524,node_4524),node_8546,(saturate((abs(i.posWorld.g)/_MaxHeight))*_EmitMul))+_EmitMin);
/// Final Color:
                float3 finalColor = diffuse + specular + emissive;
                fixed4 finalRGBA = fixed4(finalColor,1);
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
            
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #define UNITY_PASS_FORWARDADD
            #include "UnityCG.cginc"
            #include "AutoLight.cginc"
            #pragma multi_compile_fwdadd_fullshadows
            #pragma multi_compile_fog
            #pragma exclude_renderers xbox360 ps3 
            #pragma target 3.0
            uniform float4 _LightColor0;
            uniform sampler2D _Texture; uniform float4 _Texture_ST;
            uniform sampler2D _NormalMap; uniform float4 _NormalMap_ST;
            uniform float _Gloss;
            uniform float _EmitMul;
            uniform sampler2D _Ramp; uniform float4 _Ramp_ST;
            uniform float _MaxHeight;
            uniform float _EmitMin;
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
                float3 _NormalMap_var = UnpackNormal(tex2D(_NormalMap,TRANSFORM_TEX(i.uv0, _NormalMap)));
                float3 normalLocal = _NormalMap_var.rgb;
                float3 normalDirection = normalize(mul( normalLocal, tangentTransform )); // Perturbed normals
                float3 lightDirection = normalize(lerp(_WorldSpaceLightPos0.xyz, _WorldSpaceLightPos0.xyz - i.posWorld.xyz,_WorldSpaceLightPos0.w));
                float3 lightColor = _LightColor0.rgb;
                float3 halfDirection = normalize(viewDirection+lightDirection);
////// Lighting:
                float attenuation = LIGHT_ATTENUATION(i);
                float3 attenColor = attenuation * _LightColor0.xyz;
///////// Gloss:
                float gloss = _Gloss;
                float specPow = exp2( gloss * 10.0+1.0);
////// Specular:
                float NdotL = max(0, dot( normalDirection, lightDirection ));
                float4 _Texture_var = tex2D(_Texture,TRANSFORM_TEX(i.uv0, _Texture));
                float3 specularColor = ((_Texture_var.rgb*(-1.0))+1.0);
                float3 directSpecular = attenColor * pow(max(0,dot(halfDirection,normalDirection)),specPow)*specularColor;
                float3 specular = directSpecular;
/////// Diffuse:
                NdotL = max(0.0,dot( normalDirection, lightDirection ));
                float3 directDiffuse = max( 0.0, NdotL) * attenColor;
                float node_6123 = (-1*_MaxHeight);
                float node_6355 = 0.0;
                float2 node_1056 = float2(saturate((node_6355 + ( (i.posWorld.g - node_6123) * (1.0 - node_6355) ) / (_MaxHeight - node_6123))),0.0);
                float4 node_2466 = tex2D(_Ramp,TRANSFORM_TEX(node_1056, _Ramp));
                float3 node_8546 = (_Texture_var.rgb*node_2466.rgb);
                float3 diffuseColor = node_8546;
                float3 diffuse = directDiffuse * diffuseColor;
/// Final Color:
                float3 finalColor = diffuse + specular;
                fixed4 finalRGBA = fixed4(finalColor * 1,0);
                UNITY_APPLY_FOG(i.fogCoord, finalRGBA);
                return finalRGBA;
            }
            ENDCG
        }
    }
    FallBack "Diffuse"
    CustomEditor "ShaderForgeMaterialInspector"
}
