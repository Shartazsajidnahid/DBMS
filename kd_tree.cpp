// A C++ program to demonstrate operations of KD tree
#include<bits/stdc++.h>
using namespace std;

const int k = 2;
int total_height = 0;

// A structure to represent node of kd tree
struct Node
{
	int point[k]; // To store k dimensional point
	Node *left, *right;
};
struct Node *root = NULL;
// A method to create a node of K D tree
struct Node* newNode(int arr[])
{
	struct Node* temp = new Node;

	for (int i=0; i<k; i++)
	temp->point[i] = arr[i];

	temp->left = temp->right = NULL;
	return temp;
}



void insert(int point[])
{
	unsigned height = 0;

	if (root == NULL){
		int point1[] = {1, 1};
		root =  newNode(point);
	//	root->right = newNode(point1);
		return;
	}
	    
	
	struct Node* temp = root;
	struct Node* prev;

	

	int flag; 

	while(1){
		prev = temp;
		//cout << endl << temp->point[0] << " " << temp->point[1]  << endl;
		//if(temp->left==NULL) cout << " left null ";
		//else cout << "left: " << temp->left->point[0] << " " <<temp->left->point[1] ;
		//if(temp->right==NULL) cout << " right null ";
		//else cout << "right: " << temp->right->point[0] << temp->right->point[1];
		// Calculate current dimension (cd) of comparison
		unsigned cd = height % k;

		if (point[cd] < (temp->point[cd]))
			temp = temp->left, flag = 1;
		else 
			temp = temp->right, flag = 2;

		height++;

		if (temp == NULL)
			break;
	}
 	//cout << endl << endl << point[0] << "," << point[1] << " inserted ";

	if(flag==1){
		prev->left = newNode(point);
		//cout << "left " << endl;
	}
		
	else {
		prev->right = newNode(point);
	   // cout << "right " << endl;
	}
		
	if(height>total_height) total_height = height;	
}


// A utility method to determine if two Points are same
// in K Dimensional space
bool check_equal(int point1[], int point2[])
{
	// Compare individual pointinate values
	for (int i = 0; i < k; ++i)
		if (point1[i] != point2[i])
			return false;

	return true;
}

// Searches a Point represented by "point[]" in the K D tree.
// The parameter depth is used to determine current axis.

bool search(int point[]){
	unsigned height = 0;

	if (root == NULL)
	    return false;
	
	
	struct Node* temp = root;

	while(1){
		//cout << endl << temp->point[0] << " " << temp->point[1] ;
		
		if (check_equal(temp->point, point))
			return true;
		// Calculate current dimension (cd) of comparison
		unsigned cd = height % k;

		if (point[cd] < (temp->point[cd]))
			temp = temp->left;
		else 
			temp = temp->right;

		height++;

		if (temp == NULL)
			return false;
	}


}

void printTree(){
	if(root == NULL) {
		cout << endl << "Tree doesn't exist";
	}


	/*
	vector<int> points;
	vector<vector<int>> nodes;
	
	for(int i=0;i<2;i++) 
		points.push_back(root->point[i]);

	nodes.push_back(points);
	
	
	
	
	while (!nodes.empty())
	{	
		vector<int> left = nodes[0]; 
		vector<int> right = nodes[0]; 
		cout << " hey " <<  newp[0] << " " << newp[1]; 
		nodes.pop_back();
	}

	*/


}

bool search1(int point1[], int point2[]){\
	
}

void printPostorder(struct Node* node)
{
    if (node == NULL){
		cout << "null ";
		return;
	}
        


 
    // first recur on left subtree
    printPostorder(node->left);

			 // now deal with the node
	if(node==root) cout << "\t";
	cout << "{ " ;
	for(int i=0;i<k;i++)
    	cout << node->point[i] << " ";
	cout << "} " ;
	if(node==root) cout << "\t";
 
    // then recur on right subtree
    printPostorder(node->right);
 
   
}


// Driver program to test above functions
int main()
{
	
	int points[][k] = {{3, 6}, {17, 15}, {13, 15}, {6, 12},
					{9, 1}, {2, 7}, {10, 19}};

	int n = sizeof(points)/sizeof(points[0]);

	for (int i=0; i<n; i++)
		insert( points[i]);

	cout << "\nroot: " << root->point[0] << " " <<  root->point[1] << endl;

	cout << endl << "total height = " << total_height << endl;

	//printTree();
	printPostorder(root);


	cout << endl;
	 
	int point1[] = {10, 116};
	(search(point1))? cout  << "Found\n": cout << "Not Found\n";

	int point2[] = {10, 19};
	(search(point2))? cout << "Found\n": cout << "Not Found\n";

	return 0;
}
