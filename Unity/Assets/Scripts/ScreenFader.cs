using UnityEngine;
using System.Collections;

public class ScreenFader : MonoBehaviour
{
	public float fadeSpeed = 1.5f;          // Speed that the screen fades to and from black.
	
	
	public bool fadingToClear = false;
	public bool fadingToBlack = false;
	
	public CanvasRenderer panel;
	

	void Update ()
	{
		FadeToClear ();
		FadeToBlack();
	}

	public bool Play{
		set{
			fadingToClear = true;
			fadingToBlack = false;
			this.enabled = true;
		}
	}

	public bool Stop{
		set{
			fadingToClear = false;
			fadingToBlack = true;
			this.enabled = true;
		}
	}
	
	void FadeToClear ()
	{
		if(fadingToClear){
			panel.SetAlpha(Mathf.Lerp(panel.GetAlpha(), 0, fadeSpeed*Time.deltaTime));

			if(panel.GetAlpha() <= 0.05f){
				panel.SetAlpha(0f);
				this.enabled = false;
			}
		}
	}
	
	void FadeToBlack ()
	{
		if(fadingToBlack){
			panel.SetAlpha(Mathf.Lerp(panel.GetAlpha(), 1, fadeSpeed*Time.deltaTime));

			if(panel.GetAlpha() >= 0.95f){
				panel.SetAlpha(1);
				this.enabled = false;
			}
		}
	}
}