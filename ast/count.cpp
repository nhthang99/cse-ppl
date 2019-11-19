typedef binary = Struct {
    int val;
    binary *left;
    binary *right;

    int count(binary *root) {
        if (root == null) return 0;
        if (root->left == null && root->right == null) return 1;
        else return count(root->left) + count(root->right);
    }
}