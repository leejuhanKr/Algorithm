# [level 0] 겹치는 선분의 길이 - 120876 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120876) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>빨간색, 초록색, 파란색 선분이 x축 위에 있습니다. 세 선분의 x좌표 시작과 끝이 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 <code>lines</code>가 매개변수로 주어질 때,  두 개 이상의 선분이 겹치는 부분의 길이를return 하도록 solution 함수를 완성해보세요.</p>

<p><code>lines</code>가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.<br>
 <img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/4feda8d5-aa8f-4a55-8afc-db776e2f9bcd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-08-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.08.46.png" title="" alt="스크린샷 2022-08-08 오후 5.08.46.png"></p>

<p>선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 2만큼 겹쳐있습니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-100 &lt; <code>lines</code>의 원소 &lt; 100</li>
<li><code>lines</code>의 길이 = 3</li>
<li><code>lines</code>의 원소의 길이 = 2</li>
<li>모든 선분은 길이가 1 이상입니다.</li>
<li>lines의 원소는 [a, b] 형태이며, a, b는 각각 양 끝점 중 하나입니다. 

<ul>
<li>-100 &lt; a, b &lt; 100</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>lines</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0, 1], [2, 5], [3, 9]]</td>
<td>2</td>
</tr>
<tr>
<td>[[1, -1], [1, 3], [9, 3]]</td>
<td>0</td>
</tr>
<tr>
<td>[[0, 5], [3, 9], [1, 10]]</td>
<td>8</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>초록색과 파란색 선분이 [2, 5], [3, 9]로 [3, 5]만큼 겹쳐있으므로 2를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>겹친 선분이 없으므로 0을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>빨간색과 초록색 선분 [3, 5]부분이 겹칩니다.</li>
<li>빨간색과 파란색 선분 [1, 5]부분이 겹칩니다.</li>
<li>초록색과 파란색 선분이 [3, 9]부분 겹칩니다.</li>
<li>따라서 8을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges