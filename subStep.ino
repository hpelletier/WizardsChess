// This method is called in order to make the stepper motor make a number of sub steps (depending on your wiring).
// Variable steps is for number of steps (forwards = positive, backwards = negative)
// stepDelay is for waiting time between steps in microseconds => bigger means lower speed, smaller means higher speed

void subStep1(long steps, int stepDelay){

  // The function will run for the amount of times called in the method.
  // This is accomplished by a while loop, where it will subtract 1 from the amount after every run (forwards).
  // In case of backward rotation it will add 1 to the negative number of steps until 0 is reached.

  while(steps!=0)
  {

    if(steps>0){
      currStep++;
    }       //increment current halfstep (forward)
    if(steps<0){
      currStep--;
    }       //decrement current halfstep (backward)

    if(currStep>STEPS){
      currStep= currStep-STEPS;
    }         //position >360deg is reached => set position one turn back
    if(currStep<0){
      currStep= currStep+STEPS;
    }             //position <0deg   is reached => set position one turn forward

    sub = currStep%8;           //determine the next halfstep

    switch(sub)
    {
    case 0: 
      // Starting position (if repeated, ful step (4))
      // EXPLINATION: in this case, both our power are high.
      // Therefore both coils are activated, with their standard polarities for their magnetic fields.
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,HIGH);
      digitalWrite(dir1_b,HIGH);
      break;

    case 1:
      //Half step (½)
      // EXPLINATION: In this case, only out b-coil is active, still with it's stand polarity.
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,LOW);
      digitalWrite(dir1_a,HIGH);
      digitalWrite(dir1_b,LOW);
      break;

    case 2:
      //Full step (1)
      // EXPLINATION: In this case, the b-coil is activated as in previous cases.
      // But the a-coil now has it's direction turned on. So now it's active, but with the reversered polarity.
      // By continuing this pattern (for reference: http://www.8051projects.net/stepper-motor-interfacing/full-step.gif) , you'll get the axis to turn.
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,HIGH);
      digitalWrite(dir1_b,LOW);
      break;

    case 3:
      // Half step (1½)
      digitalWrite(pwr1_a,LOW);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,LOW);
      digitalWrite(dir1_b,LOW);
      break;

    case 4:
      // Full step (2)
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,LOW);
      digitalWrite(dir1_b,LOW);
      break;

    case 5:
      // Half step (2½)
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,LOW);
      digitalWrite(dir1_a,LOW);
      digitalWrite(dir1_b,LOW);
      break;

    case 6:
      // Full step (3)
      digitalWrite(pwr1_a,HIGH);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,LOW);
      digitalWrite(dir1_b,HIGH);
      break;

    case 7:
      // Half step (3½)
      digitalWrite(pwr1_a,LOW);
      digitalWrite(pwr1_b,HIGH);
      digitalWrite(dir1_a,LOW);
      digitalWrite(dir1_b,HIGH);
      break;
    }

    delayMicroseconds(stepDelay);        //Waiting time to next halfstep

    if(steps>0){
      steps--;
    }      //decrement of remaining halfsteps of forward rotation
    if(steps<0){
      steps++;
    }      //increment of remaining halfsteps of backward rotation
  }
}

void subStep2(long steps, int stepDelay){

  // The function will run for the amount of times called in the method.
  // This is accomplished by a while loop, where it will subtract 1 from the amount after every run (forwards).
  // In case of backward rotation it will add 1 to the negative number of steps until 0 is reached.

  while(steps!=0)
  {

    if(steps>0){
      currStep++;
    }       //increment current halfstep (forward)
    if(steps<0){
      currStep--;
    }       //decrement current halfstep (backward)

    if(currStep>STEPS){
      currStep= currStep-STEPS;
    }         //position >360deg is reached => set position one turn back
    if(currStep<0){
      currStep= currStep+STEPS;
    }             //position <0deg   is reached => set position one turn forward

    sub = currStep%8;           //determine the next halfstep

    switch(sub)
    {
    case 0: 
      // Starting position (if repeated, ful step (4))
      // EXPLINATION: in this case, both our power are high.
      // Therefore both coils are activated, with their standard polarities for their magnetic fields.
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,HIGH);
      digitalWrite(dir2_b,HIGH);
      break;

    case 1:
      //Half step (½)
      // EXPLINATION: In this case, only out b-coil is active, still with it's stand polarity.
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,LOW);
      digitalWrite(dir2_a,HIGH);
      digitalWrite(dir2_b,LOW);
      break;

    case 2:
      //Full step (1)
      // EXPLINATION: In this case, the b-coil is activated as in previous cases.
      // But the a-coil now has it's direction turned on. So now it's active, but with the reversered polarity.
      // By continuing this pattern (for reference: http://www.8051projects.net/stepper-motor-interfacing/full-step.gif) , you'll get the axis to turn.
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,HIGH);
      digitalWrite(dir2_b,LOW);
      break;

    case 3:
      // Half step (1½)
      digitalWrite(pwr2_a,LOW);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,LOW);
      digitalWrite(dir2_b,LOW);
      break;

    case 4:
      // Full step (2)
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,LOW);
      digitalWrite(dir2_b,LOW);
      break;

    case 5:
      // Half step (2½)
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,LOW);
      digitalWrite(dir2_a,LOW);
      digitalWrite(dir2_b,LOW);
      break;

    case 6:
      // Full step (3)
      digitalWrite(pwr2_a,HIGH);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,LOW);
      digitalWrite(dir2_b,HIGH);
      break;

    case 7:
      // Half step (3½)
      digitalWrite(pwr2_a,LOW);
      digitalWrite(pwr2_b,HIGH);
      digitalWrite(dir2_a,LOW);
      digitalWrite(dir2_b,HIGH);
      break;
    }

    delayMicroseconds(stepDelay);        //Waiting time to next halfstep

    if(steps>0){
      steps--;
    }      //decrement of remaining halfsteps of forward rotation
    if(steps<0){
      steps++;
    }      //increment of remaining halfsteps of backward rotation
  }
}
