# Problem: Mother Tux's Gold Shop

There are two sets of instructions on separate matters. You must do them both.

## INSTRUCTION SET 1: Git Repository

You must do the following:

* You must continue developing the code, creating at least TWO more commits on
  top of the template code given.
* The commit pointed by the HEAD tag must contain both files listed below.
* The file to be graded MUST be called "gold.py".
* Any files provided by the lecturer can be left in, but they will be ignored.

To configure your username and email in the Git environment, from your command
line tool, use the following commands:

```
git config user.name "Kasetsart STUDENT"
git config user.email kasetsart.st@gmail.com
```

This changes your Git username and email just for this repository.

You can use any email address as long as your name matches the actual name in
the Kasetsart University system and you are connected to the identity provided
in the GitHub Classroom environment.

You can use `git config --global ...` instead to make the commands affect
every single repo onwards.

## INSTRUCTION SET 2: Programming Problem

Following the gold price surges in 2024 and the recent drama about the quality
of gold, Tux (the Linux penguin) has a brilliant idea to also join in on the
drama and invest in a gold shop.

Unlike the other Tu\_\_, Tux is a nice proprietor (owner) and wants to be
honest about gold prices and purity. He also wants to be kind to his mother,
known as Mother Tux, but that's another story.

Mother Tux is not a very nice mother.

### DIRECTIONS:

In the file called `gold.py`, you must implement a class that represents a
piece of gold. It could be an ornament or a bar or something, doesn't matter.
It's just gold, how hard is that?

You will be guided precisely in the program file. Implement everything based
on the docstring and doctest. You can do it!

NOTE: The doctest is CORRECT but NOT NECESSARILY COMPLETE. Always check the
docstring to see what else must be implemented!

## Type Hints

To guide you to using correct data types and letting you know what can be
assumed, type hints are given in the code. See the code how it works.

See also: [[https://docs.python.org/3/library/typing.html]]

## Grading Standard

  No. | Score | Criteria
 ---- | ----- | ---------
   1  |   30  | doctest (straightforward) (-1 per failed test, min 0)
   2  |   50  | pytest 1 (basic implementation) (10 tests, 4 points/ea.)
   3  |   10  | PEP 8 (automated linter)
   4  |   10  | Repository Correctness (real name, at least 2 commits)

* Most of the problem will revolve around doing this correctly. Efficiency
  is checked in pytest 2 but is not a major part of your score.
* TA's will check for plagiarism.
* Criteria 3 may still get deducted if we find other faults not detected by
  the linter. Instructor + TA decision is final.
* For Criteria 3, your score is calculated as follows:
    score = lambda x: math.ceil((x-5) * 2)
  This means you must score at least 5 on pylint to receive score in this
  criteria!

## Notes

* Inspecting pytest files is permitted but not encouraged.
* GitHub Classroom will flag your submission if you modify the pytest file.
* Following the directions in the assignment file should be enough.

Should you accidentally commit modifications of pytest file, you can restore
it by committing everything you've done so far (leave nothing uncommitted).

Check `git log` for the very first version of the template code (that you
originally cloned from us) to see the commit ID (first 8 digits is fine)
then use the following command:

```
git checkout [Commit_ID] -- test1.py
```

Then commit again.

## Problem Author

(C) 2024 Chawanat Nakasan, Department of Computer Engineering,
Faculty of Engineering, Kasetsart University

If you found this as a forked repository, any further work is not done by the
original problem author.

Starter and tester code originally released under MIT License.

