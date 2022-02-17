// A C++ program to demonstrate operations of KD tree
#include<bits/stdc++.h>
using namespace std;
#define COUNT 10

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
		//int point1[] = {1, 1};
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


void range_search(Node* temp, int point1[], int point2[], int depth){
    // Base cases
    if (temp == NULL)
        return;

	 //  if (arePointsSame(root->point, point))
    //    return true;

	// calculating limits 

	int max[k], min[k];
	for(int i=0;i<k;i++){
		if(point1[i] < point2[i]){
			min[i] = point1[i]; max[i] = point2[i];
		}
		else {
			min[i] = point2[i]; max[i] = point1[i];
		}
	}
	
	//cout << "limits: " ;
	//for(int i=0;i<k;i++){
		
		//cout<<	min[i] << " " << max[i] << endl;
		
	//}
    // Current dimension is computed using current depth and total
    // dimensions (k)
    unsigned cd = depth % k;

    // Compare point with root with respect to cd (Current dimension)
    if (temp->point[cd] < min[cd])
         range_search(temp->right, point1, point2, depth + 1);
	else if(temp->point[cd] > max[cd])
   		 range_search(temp->left, point1, point2, depth + 1);

	else{
		int j = 0;

		for(; j<k; j++){
			//cout << "other " << temp->point[j] << " " << min[j] << " " << max[j] << endl;

			if( (min[j] > temp->point[j] ) || (max[j] < temp->point[j])){
				//cout << "broken";
				break;
			}
		}
		if(j==k){
			//cout << "hey " ;
			cout << "{";
			for(int p=0;p<k-1;p++)
				cout << temp->point[p] <<",";
			cout << temp->point[k-1] << "}" << endl;
		}
		range_search(temp->right, point1, point2, depth + 1);
		range_search(temp->left, point1, point2, depth + 1);
	}
	
}







void printTree(Node *temp, int space)
{
    // Base case
    if (temp == NULL)
        return;
 
    // Increase distance between levels
    space += COUNT;
 
    // Process right child first
    printTree(temp->right, space);
 
    // Print current node after space count
    cout<<endl;

    for (int i = COUNT; i < space; i++)
        cout<<" ";
	
	for(int i=0; i<k-1; i++)
		 cout<<temp->point[0]<<",";
	cout << temp->point[k-1];
	cout << endl; 
 
    // Process left child
    printTree(temp->left, space);
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

	//printTree(n);
	//printPostorder(root);
	printTree(root,0);

	
	cout << endl;
	 
	int point1[] = {3, 7};
	//(search(point1))? cout  << "Found\n": cout << "Not Found\n";

	int point2[] = {20, 39};
	//(search(point2))? cout << "Found\n": cout << "Not Found\n";

	cout << "ranged search: " << endl;
	range_search(root, point1, point2, 0);

	return 0;
}

