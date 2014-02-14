A little story behind solving the problem:

I started by reading the sub-questions one by one and wrote down the boolean function for each constraint.
I found those implementations were pretty straight-forward and I got a validator for any give "phone number" string. This approach has the advantage of being able to determine if a phone number is valid. So I thought it would be easy to do a search and find out all the phone numbers.

But, it turned out to be very slow.

After thinking a while, I figured I was not supposed to validate any given phone number but rather, just determine how many exists. And that seems to be a easier problem because some observation leads to that most movements are constraint to 2 options.

I restarted solving the problem and using a recursive way to calculate how many numbers are there for each length. This was also straight-forward but the advange was the computational time was decreased by a lot.

The final answer is 952.
