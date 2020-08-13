# 쉽고 빠르게 Docker 생성 및 Docker Container 내부 설정하기

glee1228@naver.com



## Docker의 기본 기능

Docker는 크게 다음의 세 가지 기능으로 분류할 수 있다.

1. Docker 이미지 생성
2. Docker 컨테이너 동작
3. Docker 이미지 공개 및 공유

Docker는 애플리케이션 실행에 필요한 프로그램, 라이브러리, 미들웨어와 OS, 네트워크 설정 등을 하나로 모아 Docker 이미지를 생성한다. 이 Docker 이미지는 실행 환경에서 동작하는 컨테이너의 기반이 된다.

이 글은 Docker 이미지 다운로드부터 이미지를 기반으로 컨테이너를 생성한 후, Docker 컨테이너가 생성된 서버와 호스트 서버가 통신 할 수 있도록 Docker 컨테이너에서 내부 설정하는 방법까지 다룬다.

 



우선, Docker를 생성하자.

## Docker 생성

1. 이미지 다운로드(pull)

   ```
   $ docker pull [OPTIONS] NAME[:TAG|@DIGEST]
   ```

   ex) docker pull -name ip_test pytorch/pytorch

   

2. 생성된 이미지 확인

   ```
   $ docker image ls
   $ docker images
   ```

   

3. 이미지를 컨테이너에 올리기

   ```
   $ nvidia-docker run -ti -p (외부포트번호):22 -v (마운트 할 폴더 경로):(컨테이너 내 마운트 된 폴더 저장 경로) --privileged --name (컨테이너 명) (이미지 명):(태그)
   $ nvidia-docker run -ti -p 7963:22 --shm-size 8G -v /media/myPC/hdd/dh:/workspace --name trn-4 pytorch/pytorch:0.4-cuda9-cudnn7-devel
   ```

   - **-ti** : bash로 시작, 만약 되지 않는다면, 맨 끝에 /bin/bash 추가
   - **--p A:B** : host의 A포트를 컨테이어의 B포트에 연결
   - **-v A:B** : host의 저장소 A 위치를 컨테이어의 저장소 B위치에 연결
   - **--name A** : 해당 컨테이너의 별명을 A로 지음
   - **--privileged** : 컨테이너 안에서 호스트의 리눅스 커널 기능을 모두 사용할 수 있도록 함
   - **--expose=[]**: 컨테이너의 포트를 호스트와 연결만 하고 외부에는 노출하지 않습니다. 예) --expose=”3306”
   - **ex) docker run -ti -p 8022:22 -p 8000:8000 -v /home/myPC:/workspace --name ubuntu_example --network myPCnet ubuntu:16.04**
     - ubuntu:16.04 이미지를 컨테이너에 올리면서, 별명은 "ubuntu_example"로 한다. 이 컨테이너는 docker network 중 myPCnet에 속하도록 한다. 이 때, host의 /home/myPC 폴더를 컨테이너 안의 /workspace와 연결한다. 또한 컨테이너의 포트 중 22번은 호스트의 8022번으로, 8000번 포트는 8000번으로 각각 포트 매핑을 시켜준다.

   

4. 컨테이너&이미지 삭제

   ```
   $ docker ps //동작중인 컨테이너 확인
   $ docker ps -a // 정지된 컨테이너 확인
   $ docker rm [container id] // 컨테이너 삭제
   ```

   ```
   $ docker rmi [image id]
   ```

   

5. 기본 명령어

   - **docker ps -a** : 현재 실행중인 모든 컨테이너 보기
   - **docker start (컨테이너 명)** : 컨테이너 시작하기
   - **docker attach (컨테이너 명)** : 컨테이너 접속하기
   - **docker stop (컨테이너 명)** : 컨테이너 중단하기
   - **docker rm (컨테이너 명)** : 컨테이너 지우기
   - **docker image ls** : 현재 가지고 있는 모든 이미지 보기
   - **docker image rm (이미지 명)** : 이미지 지우기
   - *Ctrl + P + Q* : 컨테이너 나가기
   - **exit** : 컨테이너 종료





이제부터, 생성된 Docker 컨테이너를 호스트 컴퓨터에서 SSH 프로토콜로 통신하기 위한 설정을 한다.

SSH란 Secure Shell Protocol, 즉 네트워크 프로토콜 중 하나로 컴퓨터와 컴퓨터가 인터넷과 같은 Public Network를 통해 서로 통신을 할 때 보안적으로 안전하게 통신을 하기 위해 사용하는 프로토콜이다. 대표적인 사용의 예는 다음과 같다.

1. 데이터 전송
2. 원격 제어



## Docker Container 내부 설정

1. ```
   $ apt-get update
   $ apt-get install vim
   ```

2. ```
   $ apt-get install ssh
   ```

3. ssh 키 생성

   ```
   $ cd ~/
   $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa
   ```

4. sshd를 위한 폴더 생성

   ```
   $ mkdir /var/run/sshd
   ```

5. ~/.bashrc 파일에 다음을 추가

   ```
   # autorun
   /usr/sbin/sshd
   ```

6. 변경된 사항 적용

   ```
   $ source ~/.bashrc
   ```

7. (일반) 유저 추가

   ```
   $ adduser (유저명)
   ```

   7-1. 루트 계정 비밀번호 수정

   ```
   $ passwd
   ```

   7-2. ssh 루트 계정 접속제한 해제하기

   ```
   $ vi /etc/ssh/sshd_config
   ```

   ```
   # PermitRootLogin without-password 을 아래로 변경
   PermitRootLogin yes
   ```

   ```
   $ /etc/init.d/ssh restart
   ```

8. FileZilla 접속

   sftp://IP address 로 접속

   

# 참고자료

- [가장 빨리 만나는 도커(Docker)](http://pyrasis.com/private/2014/11/30/publish-docker-for-the-really-impatient-book)
- [초보를 위한 도커 안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [컨테이너 기반 가상화 플랫폼 ‘도커(Doker)’의 이해](https://tacademy.sktechx.com/live/player/onlineLectureDetail.action?seq=125)
- [Docker 설치문서](https://github.com/sogang-mm/lab/wiki/Docker-설치-문서)
- [66.Docker Docker 컨테이너로의 sftp 사용 - filezilla를 통한 예제](https://m.blog.naver.com/PostView.nhn?blogId=alice_k106&logNo=220650722592&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
- [ssh 루트(root) 접속 제한(Permission denied) 해제하기](http://blog.naver.com/PostView.nhn?blogId=chandong83&logNo=220919303234&categoryNo=16&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=section)

출처 : https://github.com/MinjiKang95/Guide

