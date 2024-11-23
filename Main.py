import argparse
import datetime

if __name__ == "__main__":
    currID = 0
    #sets up the parser for arguments
    parser = argparse.ArgumentParser(description="A CLI Task Tracker with commands for adding, updating, deleting, and listing tasks to or in the tracker")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    #Makes an argument called add
    parser_add = subparsers.add_parser("add", help="Add a task")
    parser_add.add_argument("Description",help="The Description of the task to be added")

    parser_list = subparsers.add_parser("list", help="List all tasks or tasks with certain statuses")
    parser_list.add_argument("filter", nargs="?", choices=["done","todo","in-progress"], default=None,help="filter list by status: done, todo, in-progress")

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("tnum",help="Task # to delete", type=int)

    parser_update = subparsers.add_parser("update", help="Update a task's status")
    parser_update.add_argument("tnum",help="Task # to update",type=int)
    parser_update.add_argument("newDescription",help="The updated description of the task")

    parser_markIP = subparsers.add_parser("mark-in-progress", help="Delete a task")
    parser_markIP.add_argument("tnum",help="Task # to delete", type=int)

    parser_markdone = subparsers.add_parser("mark-done",help="Mark an item as done")
    parser_markdone.add_argument("tNum",help="Task to update",type=int)


    args = parser.parse_args()

    match(args.command):
        case add:
            currID += 1
            task = {
                id:currID,
                "description": str(args.Description),
                "status":"todo",
                "createdAt":datetime.datetime.now(),
                "updatedAT":datetime.datetime.now()
            }
            
            
