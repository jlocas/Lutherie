using UnityEngine;
using System.Collections;

public enum RandomTypes{
	max, min, tri, exp
}

[System.Serializable]
public class Pattern {

	public RandomTypes randomType;
	public int size;
	public float min;
	public float max;
	private float[] pattern;
	private int i;

	public Randoms randoms;


	public void Generate(){

		pattern = new float[size];

		switch(randomType){

		case RandomTypes.max:
			for (int i = 0; i < size; i++){
				pattern[i] = Scale( randoms.max(randoms.iter) );
			}
			break;

		case RandomTypes.min:
			for (int i = 0; i < size; i++){
				pattern[i] = Scale( randoms.min(randoms.iter) );
			}
			break;

		case RandomTypes.tri:
			for (int i = 0; i < size; i++){
				pattern[i] = Scale( randoms.tri(randoms.iter) );
			}
			break;

		case RandomTypes.exp:
			for (int i = 0; i < size; i++){
				pattern[i] = Scale( randoms.exp(randoms.steepness, randoms.dir) );
			}
			break;
		}

	}

	private float Scale(float f){
		return f * (max - min) + min;
	}

	public float ReadNext(){
		float val = pattern[i % size];
		++i;
		return val;
	}
}
