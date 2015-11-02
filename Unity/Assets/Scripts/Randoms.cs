using UnityEngine;
using System.Collections;



[System.Serializable]
public class Randoms {

	public int iter;
	public float steepness;
	public int dir;

	public float max(int iter){

		if(iter == 0){
			iter = 2;
		}

		float[] values = new float[iter];

		for(int i = 0; i < iter; i++){
			values[i] = Random.value;
		}

		return Mathf.Max(values);
	}

	public float min(int iter){
		
		if(iter == 0){
			iter = 2;
		}
		
		float[] values = new float[iter];
		
		for(int i = 0; i < iter; i++){
			values[i] = Random.value;
		}
		
		return Mathf.Min(values);
	}

	public float tri(int iter){
		
		if(iter == 0){
			iter = 2;
		}
		
		float[] values = new float[iter];
		float avg = 0f;

		for(int i = 0; i < iter; i++){
			values[i] = Random.value;
		}

		for(int i = 0; i < iter; i++){
			avg += values[i];
		}
		avg /= iter;
		return avg;
	}

	public float exp(float lambda, int dir){
		//lambda: raideur de la pente
		//dir: 0 favorise les petites valeurs, 1 les grandes
		float value = Mathf.Log10(Random.value) / lambda;

		if(dir == 1){
			return 1f - value;
		} else if (dir == 0) {
			return value;
		} else {
			Debug.Log("Randoms.exp: direction argument needs EITHER 0 or 1, please fix");
			return 0f;
		}
	}


}
