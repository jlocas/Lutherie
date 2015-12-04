using UnityEngine;
using System.Collections;

public enum MappedParameter
{
	Balls_XPos,
	Balls_ZPos,
	Balls_XSize,
	Balls_ZSize,
	Balls_MinMass,
	Balls_MaxMass,
	Balls_Frequency,
	Springs_XSpring,
	Springs_YSpring,
	Springs_ZSpring,
	Springs_XDamp,
	Springs_YDamp,
	Springs_ZDamp,
	Springs_Reposition,
	Springs_FreezeEdges,
	Springs_RepositionNOW
}

public enum Form
{
	Lin,
	Exp
}

[System.Serializable]
public class MidiController {

	public MappedParameter parameter;
	public Form form;
	public float formArg;

	SpringGrid grid;
	public SpringGrid Grid
	{
		get{
			return grid;
		}
		set{
			grid = value;
		}
	}

	Rain rain;
	public Rain BallRain{
		get{
			return rain;
		}
		set{
			rain = value;
		}
	}

	public float val;
	public float Value
	{
		get 
		{
			return val;
		}
		set
		{
			val = ApplyForm(value) * (maxVal - minVal) + minVal;
		}
	}

	public float minVal;
	public float maxVal;
	

	public void Send()	{
		switch(parameter)
		{
		case MappedParameter.Balls_Frequency:
			break;
		case MappedParameter.Balls_MaxMass:
			//rain.ballSize.max = Value;
			break;
		case MappedParameter.Balls_MinMass:
			//rain.ballSize.min = Value;
			break;
		case MappedParameter.Balls_XPos:
			//rain.CenterX = Value;
			break;
		case MappedParameter.Balls_XSize:
			rain.SizeX = Value;
			break;
		case MappedParameter.Balls_ZPos:
			//rain.CenterY = Value;
			break;
		case MappedParameter.Balls_ZSize:
			rain.SizeZ = Value;
			break;
		case MappedParameter.Springs_FreezeEdges:
			grid.freezeEdges = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_Reposition:
			grid.repositionBlocks = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_RepositionNOW:
			grid.repositionNow = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_XDamp:
			grid.damper.x = Value;
			break;
		case MappedParameter.Springs_XSpring:
			grid.spring.x = Value;
			break;
		case MappedParameter.Springs_YDamp:
			grid.damper.y = Value;
			break;
		case MappedParameter.Springs_YSpring:
			grid.spring.y = Value;
			break;
		case MappedParameter.Springs_ZDamp:
			grid.damper.z = Value;
			break;
		case MappedParameter.Springs_ZSpring:
			grid.spring.z = Value;
			break;
		}
	}

	float ApplyForm(float v){
		switch(form)
		{
		case Form.Lin:
			break;
		case Form.Exp:
			v = Mathf.Pow(formArg, v);
			break;
		}
		return v;
	}

}
