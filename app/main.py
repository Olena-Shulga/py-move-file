import os


def move_file(command: str) -> None:
    splitted_command = command.split(" ")

    if len(splitted_command) == 3:
        initial_file = splitted_command[1]
        destination_file = splitted_command[2]

        if (
                splitted_command[0] == "mv"
                and os.path.exists(initial_file)
                and initial_file != destination_file
        ):
            if "/" in destination_file:
                destination_path = destination_file.split("/")
                current_path = destination_path[0]
                for i in range(1, len(destination_path)):
                    if not os.path.exists(current_path):
                        os.mkdir(current_path)
                    current_path += "/" + destination_path[i]

            with (open(initial_file, "r") as old_file,
                  open(destination_file, "w") as new_file):
                new_file.write(old_file.read())

            os.remove(initial_file)
