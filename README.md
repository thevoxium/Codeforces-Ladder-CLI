# Codeforces-Ladder-CLI
Generate codeforces ladders in an XLS sheet using a command-line tool. Codeforces does not allow you to filter problems based on their division. Although, you can filter them based on their tags and rating. But many of us want to solve division based problems from recent contests. A2oj ladders are very old and the question pattern has significantly changed over the years.

# Steps to use the CLI

```python
git clone https://github.com/thevoxium/Codeforces-Ladder-CLI.git`
cd Codeforces-Ladder-CLI
pip3 install requirements.txt
python3 extract.py --div "B" --ir 1000 --fr 1300 --num 15
```

The last command will generate an XLS sheet with Division B problems in the rating range of [1000, 1300] of recent contests, with atmost 15 problems each, of the rating 1000, 1100, 1200, and 1300.
# Options

* `--div`: The division of problems that you need. eg. "A", "B", "C", "D", etc. **Default: "A"**
* `--ir`: Starting rating of problems. **Default: 800**
* `--fr`: Final rating of problems. **Default: 8000**
* `--num`: Numbers of problems per rating between the rating range [ir, fr]. **Default: 15**

# Example

`python3 extract.py --div "A" --ir 800 --fr 1500 --num 20`

Division A problems, in the rating range [800, 1500] with 20 problems each, of the rating 800, 900, 1000, ..., 1500.
