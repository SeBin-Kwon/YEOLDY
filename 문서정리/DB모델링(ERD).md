# 모델 ERD (22.11.09)

## 1. User

- id(or email)
- name
- password
- email
- birth
- phone_number
- sex
- followings
- like

### 1.1. Basket

- user_id
- product_id

<br/>

## 2. Products

- name
- cost
- category
- color
- size

<br/>

## 3. Community

### 3.1. QnA

- title
- content
- image
- Product
- solve
- category

### 3.2. Review

- title
- content
- image
- Product
- grade
- category

<br/>

## 4. Style

- title
- content
- image
- tag
- like