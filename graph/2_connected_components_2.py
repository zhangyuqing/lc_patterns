# LC 721: https://leetcode.com/problems/accounts-merge/

from collections import defaultdict

## Traversal
def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    email_to_name = {}
    graph = defaultdict(list)

    for curr_a in accounts:
        name, first_email = curr_a[0], curr_a[1]
        email_to_name[first_email] = name
        for email in curr_a[2:]:
            email_to_name[email] = name
            graph[first_email].append(email)
            graph[email].append(first_email)

    output = []
    visited = set()
    all_emails = list(email_to_name.keys())
    for i in range(len(all_emails)):
        curr_email = all_emails[i]
        if curr_email not in visited:
            # new component
            name = email_to_name[curr_email]
            component = []
            frontier = [curr_email]
            while frontier:
                e = frontier.pop()

                if e not in visited:
                    visited.add(e)

                    component.append(e)

                    for nb in graph[e]:
                        frontier.append(nb)

            curr_entry = [name] + sorted(component)
            output.append(curr_entry)

    return output
            

## Union Find
def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    email_to_name = {}
    root_map = {} # email: root of component email is in

    # init
    for curr_a in accounts:
        for email in curr_a[1:]:
            email_to_name[email] = curr_a[0]
            root_map[email] = email # union find init - every element is its own root

    def find(x):
        if root_map[x] != x:
            root_map[x] = find(root_map[x])
        return root_map[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        root_map[rb] = ra
        return True

    for curr_a in accounts:
        first_email = curr_a[1]
        for email in curr_a[2:]:
            union(first_email, email)

    all_emails = list(email_to_name.keys())
    connected_components = defaultdict(list) # rep: list of nodes
    for email in all_emails:
        connected_components[find(email)].append(email)

    output = []
    for key, val in connected_components.items():
        name = email_to_name[key]
        output.append([name] + sorted(val))

    return output

