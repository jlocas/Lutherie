using UnityEngine;
using System.Collections;

[System.Serializable]
public class SpringGridBlock {

	private GameObject block;
	public GameObject Block
	{ 
		get 
		{ 	
			return block; 	
		}
		set 
		{ 	
			block = value;	
		}
	}

	private GameObject anchor;
	public GameObject Anchor
	{ 
		get 
		{ 	
			return anchor; 	
		}
		set 
		{ 	
			anchor = value;	
		}
	}

	private Rigidbody body;
	public Rigidbody Body
	{ 
		get 
		{ 	
			return body; 	
		}
		set 
		{ 	
			body = value;	
		}
	}

	private BoxCollider collider;
	public BoxCollider Collider
	{ 
		get 
		{ 	
			return collider; 	
		}
		set 
		{ 	
			collider = value;	
		}
	}

	private SpringJoint[] springs;
	public SpringJoint[] Springs
	{ 
		get 
		{ 	
			return springs; 	
		}
		set 
		{ 	
			springs = value;	
		}
	}

	private bool isRepositioning;
	public bool IsRepositioning
	{ 
		get 
		{ 	
			return isRepositioning; 	
		}
		set 
		{ 	
			isRepositioning = value;	
		}
	}

	private int[] blockGroup;
	public int[] BlockGroup
	{ 
		get 
		{ 	
			return blockGroup; 	
		}
		set 
		{ 	
			blockGroup = value;	
		}
	}


}

[System.Serializable]
public class SpringGridBlockGroup
{
	private Vector3 initPos;

	private SpringGridBlock[] blocks;
	public SpringGridBlock[] Blocks
	{ 
		get 
		{ 	
			return blocks; 	
		}
		set 
		{ 	
			blocks = value;	
		}
	}
	
	public void Initialize()
	{
		initPos = GetAveragePosition();
	}
	
	public Vector3 GetAveragePosition()
	{
		Vector3 sum = new Vector3(0f,0f,0f);
		float multiplier = 1f / blocks.Length;


		foreach(SpringGridBlock blocky in blocks)
		{
			sum.x += blocky.Block.transform.position.x;
			sum.y += blocky.Block.transform.position.y;
			sum.z += blocky.Block.transform.position.z;
		}

		return new Vector3(sum.x * multiplier, sum.y * multiplier, sum.z * multiplier);
	}

	public float GetDeviation()
	{
		return Vector3.Distance(initPos, GetAveragePosition());
	}

}