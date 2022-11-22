
#  ACME

System to calculate salary from txt file

The system is built on a microkernel architecture, 
where a main class is the starting point and requests services, each module is built to satisfy a specific requirement.

Methodology:

From a general approach, it is broken down into smaller parts,
transforming them into various requirements and ensuring
its operation with unit tests and functional tests.



## Deployment

make sure have python 3+

Clone this repo

Get into the folder 

To deploy this project run

```bash
  python main.py
```

To add data, modify employes.txt file or 
change the name file in line 28 in main.py file

the format data should be like below

Example

    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00


## Authors

- [@cexperto](https://www.github.com/cexperto)

