#!/bin/bash

random_number() {
  WAIT_TIME=$[ $RANDOM % 5 + 1 ]
}

target_potential_wife() {
  echo targeting potential wife
  adb shell input tap 639 873
  adb shell input tap 639 950
  adb shell input tap 639 980
  echo target acquired
}

load_wife_retrieval_payload() {
  echo loading wife retrieval payload
  sleep 3
}

send_wife_retrieval_payload() {
  echo sending wife retrieval payload
  adb shell input tap 466 1237
  echo success
} 

prepare_for_next_potential_wife() {
  echo preparing for next wife
  random_number
  sleep $WAIT_TIME
}


for (( ; ; ))
do
  target_potential_wife
  load_wife_retrieval_payload
  send_wife_retrieval_payload
  prepare_for_next_potential_wife
done

