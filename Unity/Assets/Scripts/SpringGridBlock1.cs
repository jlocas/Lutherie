using UnityEngine;
using System.Collections;

public class SpringGridBlock1 : MonoBehaviour {
	
	private Vector3 targetPos;
	private Quaternion targetRot = new Quaternion(0f, 0f, 0f, 0f);

	public float minDistance;
	public float reposSpeed;

	private bool isRepositioning = false;

	// Use this for initialization
	void Start () {
		targetPos = gameObject.transform.position;

	
	}
	
	// Update is called once per frame
	void Update () {
		if(isRepositioning){
			Reposition();
		}

	
	}

	void Reposition()
	{
		Vector3 currentPos = gameObject.transform.position;
		float velocity = gameObject.GetComponent<Rigidbody>().velocity.magnitude;
		float distance = Vector3.Distance(currentPos, targetPos);

		BoxCollider collider = gameObject.GetComponent<BoxCollider>();


		//disable colliders if collisions prevent cube from getting home
		if (distance >= 1f && collider.enabled)
		{
			collider.enabled = false;
		} else if (distance < 0.5f && !collider.enabled && velocity < 0.01f){
			collider.enabled = true;

		}

		//fine reposition
		if(distance >= minDistance && velocity < 0.1f)
		{
			gameObject.transform.position = Vector3.Lerp(currentPos, targetPos, reposSpeed * Time.deltaTime);
		}

		else if (currentPos != targetPos && distance <= minDistance && velocity < 0.01f)
		{

			//Debug.Log("inside the rooney");
			gameObject.GetComponent<Rigidbody>().velocity = Vector3.zero;
			gameObject.GetComponent<Rigidbody>().angularVelocity = Vector3.zero;
			gameObject.transform.position = targetPos;

			Quaternion currentRot = gameObject.transform.rotation;

			if(currentRot != targetRot){
				gameObject.transform.rotation = targetRot;
			}
		}
	}

	public void SetRepositionStatus(bool status)
	{
		isRepositioning = status;
	}
}
