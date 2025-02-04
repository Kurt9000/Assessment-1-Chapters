visit = ["Japan", "Britain", "Canada", "Brazil", "France"]

print("Original list:", visit)
print("Alphabetical order:", sorted(visit))
print("List is still in its original order after sorted():", visit)
print("Reverse alphabetical order:", sorted(visit, reverse=True))
print("List after reverse sorted() call:", visit)
visit.reverse()
print("List after reverse():", visit)
visit.reverse()
print("List after second reverse():", visit)
visit.sort()
print("List after sort():", visit)
visit.sort(reverse=True)
print("List after reverse sort():", visit)