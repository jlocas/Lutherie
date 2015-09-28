using UnityEngine;
using System.Collections;

public class Ball : MonoBehaviour {

	public bool hasParticles = false;
	public GameObject particleContainer;
	public GameObject particles;

	void OnCollisionEnter()
	{
		if(!hasParticles)
		{
			GameObject newParticles = Instantiate(particles, gameObject.transform.position, Quaternion.identity) as GameObject;
			hasParticles = true;
			//newParticles.transform.SetParent(particleContainer.transform);
		}
		Destroy(gameObject);
	}

	public void SetParticleContainer(GameObject contain)
	{
		particleContainer = contain;
	}
}
