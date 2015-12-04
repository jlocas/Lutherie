Shader "Custom/HeightDependentTint_Multicolor" 
 {
   Properties 
   {
     _MainTex ("Base (RGB)", 2D) = "white" {}
     _Height1 ("Height 1", Float) = -1
     _Height2 ("Height 2", Float) = 1
     _Height3 ("Height 3", Float) = -1
     _Height4 ("Height 4", Float) = 1
     _Height5 ("Height 5", Float) = 1
     _Height6 ("Height 6", Float) = -1
     _Height7 ("Height 7", Float) = 1
     
     _Color1 ("Tint Color At 1", Color) = (0,0,0,1)
     _Color2 ("Tint Color At 2", Color) = (1,1,1,1)
     _Color3 ("Tint Color At 3", Color) = (0,0,0,1)
     _Color4 ("Tint Color At 4", Color) = (1,1,1,1)
     _Color5 ("Tint Color At 5", Color) = (1,1,1,1)
     _Color6 ("Tint Color At 6", Color) = (0,0,0,1)
     _Color7 ("Tint Color At 7", Color) = (1,1,1,1)
     
   }
  
   SubShader
   {
     Tags { "RenderType"="Opaque" }
  
     CGPROGRAM
     #pragma surface surf Lambert
  
     sampler2D _MainTex;
     fixed4 _Color1;
     fixed4 _Color2;
     fixed4 _Color3;
     fixed4 _Color4;
     fixed4 _Color5;
     fixed4 _Color6;
     fixed4 _Color7;
     
     float _Height1;
     float _Height2;
     float _Height3;
     float _Height4;
     float _Height5;
     float _Height6;
     float _Height7;
       
     struct Input
     {
       float2 uv_MainTex;
       float3 worldPos;
     };
  
     void surf (Input IN, inout SurfaceOutput o) 
     {
       half4 c = tex2D (_MainTex, IN.uv_MainTex);
       float posY = IN.worldPos.y;
       fixed4 tintColor;
       
       if(IN.worldPos.y > _Height1 && IN.worldPos.y <= _Height2)
       {
       		float h = (_Height2-IN.worldPos.y) / (_Height2-_Height1);
       		tintColor = lerp(_Color2.rgba, _Color1.rgba, h);
       } 
       else if(IN.worldPos.y > _Height2 && IN.worldPos.y <= _Height3)
       {
       		float h = (_Height3-IN.worldPos.y) / (_Height3-_Height2);
       		tintColor = lerp(_Color3.rgba, _Color2.rgba, h);
       }
       else if(IN.worldPos.y > _Height3 && IN.worldPos.y <= _Height4)
       {
            float h = (_Height4-IN.worldPos.y) / (_Height4-_Height3);
       		tintColor = lerp(_Color4.rgba, _Color3.rgba, h);
       }
       else if(IN.worldPos.y > _Height4 && IN.worldPos.y <= _Height5)
       {
            float h = (_Height5-IN.worldPos.y) / (_Height5-_Height4);
       		tintColor = lerp(_Color5.rgba, _Color4.rgba, h);
       }
       else if(IN.worldPos.y > _Height5 && IN.worldPos.y <= _Height6)
       {
            float h = (_Height6-IN.worldPos.y) / (_Height6-_Height5);
       		tintColor = lerp(_Color6.rgba, _Color5.rgba, h);
       }
       else if(IN.worldPos.y > _Height6 && IN.worldPos.y <= _Height7)
       {
            float h = (_Height7-IN.worldPos.y) / (_Height7-_Height6);
       		tintColor = lerp(_Color7.rgba, _Color6.rgba, h);
       }
       else if(IN.worldPos.y > _Height7)
       {
       		tintColor = _Color7;
       }
       else if(IN.worldPos.y < _Height1)
       {
       		tintColor = _Color1;
       }

       o.Albedo = c.rgb * tintColor.rgb;
       o.Alpha = c.a * tintColor.a;
     }
     ENDCG
   } 
   Fallback "Diffuse"
 }