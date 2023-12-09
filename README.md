# MultipurposeWebTool

## Use the spec-file.txt to install its listed packages into a conda environment

```conda create --name myenv --file spec-file.txt```

## Do migrations with the below command for all the folloing projects: admin, auth, contnettypes, notes, register, sessions, todo, weather

```python manage.py migrate <project-name>```
