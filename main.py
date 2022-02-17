financial= int(input("What is your monthly income?"))
meal= input("Are you taking the Commuter Meal plan?")
trnsprt_r= str(input("Will you use public transportation or private transportation?"))
if trnsprt_r== "private":
  trnsprt_cost= int(input("What is your montly estimated transportation expense?"))
elif trnsprt_r== "both":
  trnsprt_cost= int(input("What is your montly estimated transportation expense?")) + 82
elif trnsprt_r== "public":
  trnsprt_cost= 82
  