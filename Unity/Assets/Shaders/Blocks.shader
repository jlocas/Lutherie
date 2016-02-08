// Shader created with Shader Forge v1.21 
// Shader Forge (c) Neat Corporation / Joachim Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.21;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,lico:1,lgpr:1,limd:1,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:0,bdst:1,dpts:2,wrdp:True,dith:0,rfrpo:True,rfrpn:Refraction,coma:15,ufog:True,aust:True,igpj:False,qofs:0,qpre:1,rntp:1,fgom:False,fgoc:False,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False;n:type:ShaderForge.SFN_Final,id:1,x:34817,y:32664,varname:node_1,prsc:2|diff-8546-OUT,spec-9318-OUT,gloss-1673-OUT,normal-5954-RGB,emission-434-OUT;n:type:ShaderForge.SFN_Tex2d,id:9026,x:33033,y:32416,ptovrint:False,ptlb:Texture,ptin:_Texture,varname:node_9026,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:fea5724c6050dc249be20446ba456d42,ntxv:0,isnm:False|UVIN-3062-UVOUT;n:type:ShaderForge.SFN_TexCoord,id:3062,x:32785,y:32615,varname:node_3062,prsc:2,uv:0;n:type:ShaderForge.SFN_Tex2d,id:5954,x:33033,y:32615,ptovrint:False,ptlb:Normal Map,ptin:_NormalMap,varname:_Texture_copy,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:ff2741e3237de83498f28f6e738af8fb,ntxv:3,isnm:True|UVIN-3062-UVOUT;n:type:ShaderForge.SFN_Multiply,id:5121,x:33706,y:32224,varname:node_5121,prsc:2|A-6117-OUT,B-4751-OUT;n:type:ShaderForge.SFN_Vector1,id:4751,x:33552,y:32258,varname:node_4751,prsc:2,v1:-1;n:type:ShaderForge.SFN_Add,id:9318,x:33999,y:32224,varname:node_9318,prsc:2|A-5121-OUT,B-5097-OUT;n:type:ShaderForge.SFN_Vector1,id:5097,x:33843,y:32258,varname:node_5097,prsc:2,v1:1;n:type:ShaderForge.SFN_Relay,id:6117,x:33496,y:32224,varname:node_6117,prsc:2|IN-9026-RGB;n:type:ShaderForge.SFN_ValueProperty,id:1673,x:34252,y:32741,ptovrint:False,ptlb:Gloss,ptin:_Gloss,varname:node_1673,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1.3;n:type:ShaderForge.SFN_ValueProperty,id:6922,x:31128,y:32908,ptovrint:False,ptlb:Height 1,ptin:_Height1,varname:node_6922,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:-1;n:type:ShaderForge.SFN_ValueProperty,id:7241,x:31128,y:33037,ptovrint:False,ptlb:Height 2,ptin:_Height2,varname:_Height2,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1;n:type:ShaderForge.SFN_Color,id:5314,x:31611,y:33515,ptovrint:False,ptlb:Color 1,ptin:_Color1,varname:node_5314,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:0,c2:1,c3:0.006896496,c4:1;n:type:ShaderForge.SFN_Color,id:4999,x:31611,y:33687,ptovrint:False,ptlb:Color 2,ptin:_Color2,varname:_Color2,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:0,c2:0.1724138,c3:1,c4:1;n:type:ShaderForge.SFN_Multiply,id:8546,x:33634,y:32811,varname:node_8546,prsc:2|A-9026-RGB,B-2756-OUT;n:type:ShaderForge.SFN_ValueProperty,id:9969,x:31128,y:33168,ptovrint:False,ptlb:Height 3,ptin:_Height3,varname:_Height3,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:3;n:type:ShaderForge.SFN_Color,id:2264,x:31611,y:33852,ptovrint:False,ptlb:Color 3,ptin:_Color3,varname:_Color3,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:0,c3:0,c4:1;n:type:ShaderForge.SFN_Color,id:1803,x:31611,y:34019,ptovrint:False,ptlb:Color 4,ptin:_Color4,varname:_Color4,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:0.9310346,c3:0,c4:1;n:type:ShaderForge.SFN_Color,id:2143,x:31611,y:34191,ptovrint:False,ptlb:Color 5,ptin:_Color5,varname:_Color5,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:0,c2:0.8344827,c3:1,c4:1;n:type:ShaderForge.SFN_ValueProperty,id:7703,x:31128,y:33302,ptovrint:False,ptlb:Height 4,ptin:_Height4,varname:_Height4,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:5;n:type:ShaderForge.SFN_ValueProperty,id:1371,x:31128,y:33434,ptovrint:False,ptlb:Height 5,ptin:_Height5,varname:_Height5,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:7;n:type:ShaderForge.SFN_InverseLerp,id:2227,x:31592,y:32720,varname:node_2227,prsc:2|A-6922-OUT,B-7241-OUT,V-5931-Y;n:type:ShaderForge.SFN_InverseLerp,id:8779,x:31592,y:32849,varname:node_8779,prsc:2|A-7241-OUT,B-9969-OUT,V-5931-Y;n:type:ShaderForge.SFN_InverseLerp,id:9717,x:31592,y:32980,varname:node_9717,prsc:2|A-9969-OUT,B-7703-OUT,V-5931-Y;n:type:ShaderForge.SFN_InverseLerp,id:4520,x:31592,y:33114,varname:node_4520,prsc:2|A-7703-OUT,B-1371-OUT,V-5931-Y;n:type:ShaderForge.SFN_Lerp,id:791,x:32353,y:33119,varname:node_791,prsc:2|A-5314-RGB,B-4999-RGB,T-1491-OUT;n:type:ShaderForge.SFN_Lerp,id:5704,x:32347,y:33450,varname:node_5704,prsc:2|A-4999-RGB,B-2264-RGB,T-3772-OUT;n:type:ShaderForge.SFN_Lerp,id:2442,x:32347,y:33755,varname:node_2442,prsc:2|A-2264-RGB,B-1803-RGB,T-2337-OUT;n:type:ShaderForge.SFN_Lerp,id:5739,x:32347,y:34058,varname:node_5739,prsc:2|A-1803-RGB,B-2143-RGB,T-965-OUT;n:type:ShaderForge.SFN_Ceil,id:8650,x:32353,y:32992,varname:node_8650,prsc:2|IN-1491-OUT;n:type:ShaderForge.SFN_Multiply,id:3636,x:32551,y:33119,varname:node_3636,prsc:2|A-5984-OUT,B-791-OUT;n:type:ShaderForge.SFN_Ceil,id:5922,x:32347,y:33322,varname:node_5922,prsc:2|IN-3772-OUT;n:type:ShaderForge.SFN_Multiply,id:3065,x:32551,y:33450,varname:node_3065,prsc:2|A-1113-OUT,B-5704-OUT;n:type:ShaderForge.SFN_Ceil,id:1991,x:32347,y:33629,varname:node_1991,prsc:2|IN-2337-OUT;n:type:ShaderForge.SFN_Ceil,id:6719,x:32347,y:33937,varname:node_6719,prsc:2|IN-965-OUT;n:type:ShaderForge.SFN_Multiply,id:483,x:32546,y:33755,varname:node_483,prsc:2|A-4254-OUT,B-2442-OUT;n:type:ShaderForge.SFN_Multiply,id:8826,x:32546,y:33937,varname:node_8826,prsc:2|A-6719-OUT,B-5739-OUT;n:type:ShaderForge.SFN_Add,id:2756,x:33017,y:33110,varname:node_2756,prsc:2|A-3636-OUT,B-3065-OUT,C-483-OUT,D-8826-OUT,E-7576-OUT;n:type:ShaderForge.SFN_Clamp01,id:1491,x:32166,y:32992,varname:node_1491,prsc:2|IN-2227-OUT;n:type:ShaderForge.SFN_Clamp01,id:3772,x:32158,y:33322,varname:node_3772,prsc:2|IN-8779-OUT;n:type:ShaderForge.SFN_Clamp01,id:2337,x:32157,y:33629,varname:node_2337,prsc:2|IN-9717-OUT;n:type:ShaderForge.SFN_Clamp01,id:965,x:32163,y:33937,varname:node_965,prsc:2|IN-4520-OUT;n:type:ShaderForge.SFN_Subtract,id:5984,x:32551,y:32992,varname:node_5984,prsc:2|A-8650-OUT,B-5922-OUT;n:type:ShaderForge.SFN_Subtract,id:1113,x:32551,y:33322,varname:node_1113,prsc:2|A-5922-OUT,B-1991-OUT;n:type:ShaderForge.SFN_Subtract,id:4254,x:32546,y:33629,varname:node_4254,prsc:2|A-1991-OUT,B-6719-OUT;n:type:ShaderForge.SFN_If,id:7576,x:32551,y:32844,varname:node_7576,prsc:2|A-5931-Y,B-6922-OUT,GT-599-OUT,EQ-599-OUT,LT-5314-RGB;n:type:ShaderForge.SFN_Vector1,id:599,x:32389,y:32878,varname:node_599,prsc:2,v1:0;n:type:ShaderForge.SFN_ValueProperty,id:532,x:33526,y:33624,ptovrint:False,ptlb:Max Emit Height,ptin:_MaxEmitHeight,varname:node_532,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:5;n:type:ShaderForge.SFN_Divide,id:2052,x:33701,y:33590,varname:node_2052,prsc:2|A-3631-OUT,B-532-OUT;n:type:ShaderForge.SFN_Clamp01,id:9803,x:33863,y:33590,varname:node_9803,prsc:2|IN-2052-OUT;n:type:ShaderForge.SFN_Lerp,id:434,x:34241,y:33473,varname:node_434,prsc:2|A-4524-OUT,B-5573-OUT,T-2115-OUT;n:type:ShaderForge.SFN_Vector1,id:4524,x:34010,y:33473,varname:node_4524,prsc:2,v1:0;n:type:ShaderForge.SFN_Abs,id:3631,x:33701,y:33442,varname:node_3631,prsc:2|IN-6226-Y;n:type:ShaderForge.SFN_ObjectPosition,id:5595,x:31128,y:32585,varname:node_5595,prsc:2;n:type:ShaderForge.SFN_FragmentPosition,id:5931,x:31127,y:32734,varname:node_5931,prsc:2;n:type:ShaderForge.SFN_FragmentPosition,id:6226,x:33526,y:33442,varname:node_6226,prsc:2;n:type:ShaderForge.SFN_ValueProperty,id:5331,x:33863,y:33745,ptovrint:False,ptlb:Emit Strength,ptin:_EmitStrength,varname:node_5331,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:1;n:type:ShaderForge.SFN_Multiply,id:2115,x:34041,y:33590,varname:node_2115,prsc:2|A-9803-OUT,B-5331-OUT;n:type:ShaderForge.SFN_Relay,id:5573,x:34010,y:33531,varname:node_5573,prsc:2|IN-8546-OUT;n:type:ShaderForge.SFN_ViewReflectionVector,id:1406,x:34181,y:32850,varname:node_1406,prsc:2;proporder:9026-5954-1673-6922-7241-9969-7703-1371-5314-4999-2264-1803-2143-532-5331;pass:END;sub:END;*/

Shader "Shader Forge/Blocks" {
    Properties {
        _Texture ("Texture", 2D) = "white" {}
        _NormalMap ("Normal Map", 2D) = "bump" {}
        _Gloss ("Gloss", Float ) = 1.3
        _Height1 ("Height 1", Float ) = -1
        _Height2 ("Height 2", Float ) = 1
        _Height3 ("Height 3", Float ) = 3
        _Height4 ("Height 4", Float ) = 5
        _Height5 ("Height 5", Float ) = 7
        _Color1 ("Color 1", Color) = (0,1,0.006896496,1)
        _Color2 ("Color 2", Color) = (0,0.1724138,1,1)
        _Color3 ("Color 3", Color) = (1,0,0,1)
        _Color4 ("Color 4", Color) = (1,0.9310346,0,1)
        _Color5 ("Color 5", Color) = (0,0.8344827,1,1)
        _MaxEmitHeight ("Max Emit Height", Float ) = 5
        _EmitStrength ("Emit Strength", Float ) = 1
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
            uniform float _Height1;
            uniform float _Height2;
            uniform float4 _Color1;
            uniform float4 _Color2;
            uniform float _Height3;
            uniform float4 _Color3;
            uniform float4 _Color4;
            uniform float4 _Color5;
            uniform float _Height4;
            uniform float _Height5;
            uniform float _MaxEmitHeight;
            uniform float _EmitStrength;
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
                float node_1491 = saturate(((i.posWorld.g-_Height1)/(_Height2-_Height1)));
                float node_3772 = saturate(((i.posWorld.g-_Height2)/(_Height3-_Height2)));
                float node_5922 = ceil(node_3772);
                float node_2337 = saturate(((i.posWorld.g-_Height3)/(_Height4-_Height3)));
                float node_1991 = ceil(node_2337);
                float node_965 = saturate(((i.posWorld.g-_Height4)/(_Height5-_Height4)));
                float node_6719 = ceil(node_965);
                float node_7576_if_leA = step(i.posWorld.g,_Height1);
                float node_7576_if_leB = step(_Height1,i.posWorld.g);
                float node_599 = 0.0;
                float3 node_8546 = (_Texture_var.rgb*(((ceil(node_1491)-node_5922)*lerp(_Color1.rgb,_Color2.rgb,node_1491))+((node_5922-node_1991)*lerp(_Color2.rgb,_Color3.rgb,node_3772))+((node_1991-node_6719)*lerp(_Color3.rgb,_Color4.rgb,node_2337))+(node_6719*lerp(_Color4.rgb,_Color5.rgb,node_965))+lerp((node_7576_if_leA*_Color1.rgb)+(node_7576_if_leB*node_599),node_599,node_7576_if_leA*node_7576_if_leB)));
                float3 diffuseColor = node_8546;
                float3 diffuse = (directDiffuse + indirectDiffuse) * diffuseColor;
////// Emissive:
                float node_4524 = 0.0;
                float3 emissive = lerp(float3(node_4524,node_4524,node_4524),node_8546,(saturate((abs(i.posWorld.g)/_MaxEmitHeight))*_EmitStrength));
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
            uniform float _Height1;
            uniform float _Height2;
            uniform float4 _Color1;
            uniform float4 _Color2;
            uniform float _Height3;
            uniform float4 _Color3;
            uniform float4 _Color4;
            uniform float4 _Color5;
            uniform float _Height4;
            uniform float _Height5;
            uniform float _MaxEmitHeight;
            uniform float _EmitStrength;
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
                float node_1491 = saturate(((i.posWorld.g-_Height1)/(_Height2-_Height1)));
                float node_3772 = saturate(((i.posWorld.g-_Height2)/(_Height3-_Height2)));
                float node_5922 = ceil(node_3772);
                float node_2337 = saturate(((i.posWorld.g-_Height3)/(_Height4-_Height3)));
                float node_1991 = ceil(node_2337);
                float node_965 = saturate(((i.posWorld.g-_Height4)/(_Height5-_Height4)));
                float node_6719 = ceil(node_965);
                float node_7576_if_leA = step(i.posWorld.g,_Height1);
                float node_7576_if_leB = step(_Height1,i.posWorld.g);
                float node_599 = 0.0;
                float3 node_8546 = (_Texture_var.rgb*(((ceil(node_1491)-node_5922)*lerp(_Color1.rgb,_Color2.rgb,node_1491))+((node_5922-node_1991)*lerp(_Color2.rgb,_Color3.rgb,node_3772))+((node_1991-node_6719)*lerp(_Color3.rgb,_Color4.rgb,node_2337))+(node_6719*lerp(_Color4.rgb,_Color5.rgb,node_965))+lerp((node_7576_if_leA*_Color1.rgb)+(node_7576_if_leB*node_599),node_599,node_7576_if_leA*node_7576_if_leB)));
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
