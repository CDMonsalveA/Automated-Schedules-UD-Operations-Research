# Matematical Model Using Operations Research

## Sets

- $c$: Classroom | $c = {1,2,3,...,C}$

- $g$: Group | $g = {1,2,3,...,G}$

- $p$: Project | $p = {1,2,3,...,P}$

- $d$: Day | $d = {1,2,3,...,D}$

## Variables

- $$X_{c,g,p,d} = \begin{cases} 1 & \text{if a classroom $c$ is assigned to a group $g$ of a project $p$ on a day $d$} \\ 0 & \text{otherwise} \end{cases}$$

## Parameters

- $H_{d}$: Number of hours on day $d$

- $R_{p,g,d}$: Requirement of project $p$ of group $g$ on day $d$ in hours per week

- $Gr_{c,g}$: Grouper of classroom $c$ and group $g$

  - $$Gr_{c,g} = \begin{cases} 1 & \text{if a classroom $c$ can satisfy the need of a group $g$} \\ 0 & \text{otherwise} \end{cases}$$

- $W_{c,g,p,d}$: Weight of classroom $c$ and group $g$ on day $d$ for project $p$

## Objective

- Minimize the number of classrooms used

  - $$\min \sum_{c,g,p,d} \frac{1}{W_{c,g,p,d}} \cdot X_{c,g,p,d}$$

## Constraints

1. A group can only be assigned once per classroom, per project, per day $$\sum_{c} X_{c,g,p,d} \leq 1 \quad \forall g,p,d$$

2. An assigned classroom must be able to satisfy the need of a group $$X_{c,g,p,d} \leq Gr_{c,g} \quad \forall c,g,p,d$$

3. A Project may only count one group per classroom, per day $$\sum_{g,p} X_{c,g,p,d} \leq 1 \quad \forall c,d$$

4. The assignment of a classroom to a group to a project to a day must satisfy the requirement $$\sum_{c} X_{c,g,p,d} \cdot H_{d} \geq R_{p,g,d} \quad \forall g,p,d$$

add weight to make them more accesible on movements
clases del m,ismo semestre
profesor en el mismo salón
pensar en la ocupación de sillas

