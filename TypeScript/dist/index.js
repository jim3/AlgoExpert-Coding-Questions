"use strict";
class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
// Method to insert values into the BST
insert(value, number);
void {
    : .value
};
{
    if (this.left === null) {
        this.left = new BST(value);
    }
    else {
        this.left.insert(value);
    }
}
{
    if (this.right === null) {
        this.right = new BST(value);
    }
    else {
        this.right.insert(value);
    }
}
// Method to find the closest value in the BST
findClosestValue(target, number);
number;
{
    return this._findClosestValueHelper(target, Infinity);
}
_findClosestValueHelper(target, number, closest, number);
number;
{
    if (this === null) {
        return closest;
    }
    if (Math.abs(target - closest) > Math.abs(target - this.value)) {
        closest = this.value;
    }
    if (target < this.value) {
        if (this.left !== null) {
            return this.left._findClosestValueHelper(target, closest);
        }
    }
    else if (target > this.value) {
        if (this.right !== null) {
            return this.right._findClosestValueHelper(target, closest);
        }
    }
    return closest;
}
// Create a BST and insert values
let root = new BST(10);
root.insert(5);
root.insert(2);
root.insert(5);
root.insert(1);
root.insert(15);
root.insert(13);
root.insert(22);
root.insert(14);
// Call the findClosestValue method
const target = 12;
const closestValue = root.findClosestValue(target);
console.log(`The closest value to ${target} in the BST is ${closestValue}`);
