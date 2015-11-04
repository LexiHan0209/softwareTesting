# Tinydb Test Plan

**Author**: Xiqian Han, Yingyu Wu, Xu Han

**Email** : xhan5@kent.edu, ywu23@kent.edu, xhan9@kent.edu

## 1 Testing Strategy

### 1.1 Overall strategy

In order to test the Tinydb, our testing strategy will involve the system test. The system tests will be conducted as outlined in the “Test Cases” section below.

### 1.2 Test Selection

We will employ a black-box technique for the system tests (i.e., testing the functionality of the system without peering into the inner workings).

### 1.3 Test Criterion

System tests will be assessed by functional coverage, and it should cover most of the usercase with one or more system tests.

#### Funcational Test

1) Database connection

2) Query

3) Data type 

#### No-Functional Test


1) Speed. The system should be able to return the result in 3 seconds.

2) Convenient. It should be easier for user to interact with it.
  


## 2 Test Cases

| # | Test Name | Purpose |  Expected Value | Actual Result | Pass/Fail |
|:-:|:----------|:--------|:----------------|:--------------|:---------:|
| 1 | Database Connection| Confirm the client interface can connect to the database correctly | Connect correctly||
| 2 | Search/Insert/Modify/Delete the data which is existing by Valid query | Confirm the query can function correctly | return the expect result ||
| 3 | Search/Insert/Modify/Delete the data which is existing by invalid query | Confirm the query can function correctly | return error message to client ||
| 4 | Search/Insert/Modify/Delete the data which is <b>NOT</b> existing by valid query | Confirm the query can function correctly | return not finding message to client ||
| 5 | Search/Insert/Modify/Delete the data which is <b>NOT</b> existing by invalid query | Confirm the query can function correctly | return error message to client ||
| 6 | Search/Insert/Modify/Delete the data which is <b>NOT</b> existing by invalid query | Confirm the query can function correctly | return error message to client ||
| 7 | Event-based queires | Confirm the the event based query can function correctly | The event based query allow system to be dormant until some external conditions occurs， instead of continually polling or blocking on an iterator waiting for some data to arrive ||
| 8 | Boundary testing |  Check the system can handle boundary overflow | The systemn should stop the request and return the "boundary overflow" message to the client||
| 9| Data type testing | System should handle the invalid input data type  | The systemn should stop the request and return the "invalid data type" message to the client||














