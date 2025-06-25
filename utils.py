def parse_time(time_str):
    time_str = time_str.lower()
    hours = 0
    minutes = 0
    if 'h' in time_str:
        parts = time_str.split('h')
        hours = int(parts[0].strip())
        time_str = parts[1]
    if 'm' in time_str:
        minutes = int(time_str.split('m')[0].strip())
    return hours * 60 + minutes
