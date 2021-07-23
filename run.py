f = open("output.txt", "a")
check = ["Refund", "$10", "20", "Jan", "For", "Cash",
         "Mar", "Chase", "Declined", "Feb", "Add", "SERENYTY"]
lines_seen = set()
with open("input.txt") as output_file_handle:
    for out_line in output_file_handle:
        out_array = out_line.split(" ")
        count = len(out_array)
        if (count == 2):
            if (out_array[0] not in check and out_array[1] not in check and "$" not in out_array[0] and "$" not in out_array[1] and "Declined" not in out_array[0] and "Declined" not in out_array[1] and "Refunding" not in out_array[0] and "Refunding" not in out_array[1] and "Failed" not in out_array[1]):
                try:
                    with open("output.txt") as output_file_handle_2:
                        if out_line not in lines_seen: # not a duplicate
                            lines_seen.add(out_line)
                            f.writelines(out_line)
                except:
                    print("An exception occurred")
