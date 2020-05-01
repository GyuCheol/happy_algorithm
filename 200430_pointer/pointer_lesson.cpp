#include <iostream>
#include <vector>

using namespace std;

struct Student
{
	int age;
	int math;
};

void func(Student t) // 값 복사
{

}

void func(Student* t) // 4 bytes
{

}

int main()
{
	vector<Student> student_vector;

	student_vector.push_back({ 17, 100 });
	student_vector.push_back({ 18, 97 });
	student_vector.push_back({ 16, 78 });

	// python처럼 순회
	for (Student s : student_vector)
	{
		// 값 복사가 일어남!!
		s.age = 20;
		// 실제 데이터에 영향을 1도 안줌!!!
	}

	for (Student s : student_vector)
	{
		cout << s.age << endl;
	}

	// 참조를 통한 순회 (포인터와 비슷)
	for (Student& s : student_vector)
	{
		// 실제 vector 데이터에 영향을 줌.
		// 값 복사가 일어나지 않음!!
		s.age = 20;
	}

	// iterator를 이용한 순회
	// Student의 포인터다!
	auto it = student_vector.begin(); // pointer로 첫 번째 요소 주소를 가져옴.

	while (it != student_vector.end())
	{
		cout << it->age << endl;
		it++; // 그 다음 요소의 위치로 이동
	}

	return 0;
}

