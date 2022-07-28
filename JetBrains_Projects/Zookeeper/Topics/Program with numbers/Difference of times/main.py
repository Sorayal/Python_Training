first_event_hours = int(input())
first_event_minutes = int(input())
first_event_seconds = int(input())
second_event_hours = int(input())
second_event_minutes = int(input())
second_event_seconds = int(input())

start_seconds = first_event_seconds + first_event_minutes * 60 + first_event_hours * 60 * 60
end_seconds = second_event_seconds + second_event_minutes * 60 + second_event_hours * 60 * 60
print(abs(end_seconds - start_seconds))
