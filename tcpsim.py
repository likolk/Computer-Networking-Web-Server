SYN_STR = "SYN"
ACK_STR = "ACK"
FIN_STR = "FIN"
SEQ_VALUE = "Seq"
ACK_VALUE = "Ack"

def make_string(flags, values):
    """
    Create a simulated TCP message with the given flags, seq number and ack number
    """
    flags_str = ""
    if isinstance(flags, str):
        flags_str += flags
    else:
        comma = False
        for flag in flags:
            if comma:
                flags_str += ","
            flags_str += flag
            comma = True
    for value in values:
        flags_str += " " + value + "=" + str(values[value])
    return flags_str

def parse_string(str):
    """
    Parse a recieved string to get its "Seq" and "Ack" numbers
    """
    values = str.split(" ")
    out = {}
    for value in values:
        v = value.split("=")
        if (len(v) == 2):
            out[v[0]] = int(v[1])
    return out

def next_segment(values):
    """
    Given the "Syn" and "Ack" numbers from a server message, returns values for the next segment to send
    to that server
    """
    temp = values[SEQ_VALUE]
    values[SEQ_VALUE] = values[ACK_VALUE]
    values[ACK_VALUE] = temp + 1
    return values
