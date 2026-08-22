def monitor_following_distance(distances: list[float], speeds: list[float]) -> tuple[int, float, int]:

 if len(distances) == 0 :
  return (0, 0.0, 0)

 minimum = distances[0] 
 was_tailgating = False 
 now_tailgating = False 
 tailgating_seconds = 0 
 incident_counter = 0

 for i in range(len(distances)) :
  safe_distance = speeds[i] * 0.5
 
  if distances[i] < safe_distance :
   tailgating_seconds+=1
   now_tailgating = True

  if distances[i] < minimum :
   minimum = distances[i]

  if now_tailgating == True and was_tailgating == False :
   incident_counter+=1

  was_tailgating = now_tailgating 
  now_tailgating = False

 return(tailgating_seconds, minimum, incident_counter)

