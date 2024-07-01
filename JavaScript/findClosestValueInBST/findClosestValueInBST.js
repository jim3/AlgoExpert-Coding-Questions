// This is the class of the input tree.
class BST {
	constructor(value) {
	  this.value = value;
	  this.left = null;
	  this.right = null;
	}
  }
  
  function findClosestValueInBst(tree, target) {
	return bstHelper(tree, target, Infinity);
  }
  
  function bstHelper(tree, target, closest) {
	if (tree === null) {
	  return closest;
	}
	if (Math.abs(target - closest) > Math.abs(target - tree.value)) {
	  closest = tree.value;
	}
	if (target < tree.value) {
	  return bstHelper(tree.left, target, closest);
	} else if (target > tree.value) {
	  return bstHelper(tree.right, target, closest);
	} else {
	  return closest;
	}
  }
  
  function insertIntoBst(tree, value) {
	if (tree === null) {
	  return new BST(value);
	}
	if (value < tree.value) {
	  tree.left = insertIntoBst(tree.left, value);
	} else {
	  tree.right = insertIntoBst(tree.right, value);
	}
	return tree;
  }
  
  // Create a BST and insert values
  let root = new BST(10);
  insertIntoBst(root, 5);
  insertIntoBst(root, 2);
  insertIntoBst(root, 5);
  insertIntoBst(root, 1);
  insertIntoBst(root, 15);
  insertIntoBst(root, 13);
  insertIntoBst(root, 22);
  insertIntoBst(root, 14);
  
  // Call the findClosestValueInBst function
  const target = 12;
  const closestValue = findClosestValueInBst(root, target);
  console.log(`The closest value to ${target} in the BST is ${closestValue}`);
  