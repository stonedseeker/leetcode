import java.util.*;

class Employee {
  String job_title;
  float salary;

  Employee(String job_title, float salary) {
    this.job_title = job_title;
    this.salary = salary;
  }

  public float total_salary() {
    this.salary = this.salary - this.salary / 10;
    return this.salary;   
  } 

  public float update_salary() {
    Scanner sc = new Scanner(System.in);
    float update = sc.nextFloat();
    this.salary = this.salary + update;
    return this.salary;
  }

  public void tell_details() {
    System.out.print(this.salary + " ");
    System.out.println(this.job_title);
  }

  public static void main(String[] args) {
    Employee vaibhav = new Employee("Senior Developer", 500000);

    vaibhav.tell_details();

    System.out.println(vaibhav.total_salary());
    System.out.println(vaibhav.update_salary());


  }
}
