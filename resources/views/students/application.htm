<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{{ env('APP_NAME') }}</title>
    <!-- plugins:css -->
    <link rel="stylesheet" href="{{ asset('/assets/vendors/mdi/css/materialdesignicons.min.css')}}">
    <link rel="stylesheet" href="{{asset('/assets/css/style.css')}}">
    <!-- End layout styles -->
    <link rel="shortcut icon" href="{{ asset('/assets/images/favicon.ico') }}" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
      </head>
  <body>

      <!-- partial:partials/_navbar.html -->
      <nav class="navbar default-layout-navbar col-lg-12 col-12 p-0 fixed-top d-flex flex-row">
        <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-center">
          <a class="navbar-brand brand-logo" href="{{ route('students.view') }}">{{ env('APP_NAME') }}</a
        </div>
        <div class="navbar-menu-wrapper d-flex align-items-stretch">
          <button class="navbar-toggler navbar-toggler align-self-center" type="button" data-toggle="minimize">
            <span class="mdi mdi-menu m-4"></span>
          </button>
          <ul class="navbar-nav navbar-nav-right">
            <li class="nav-item nav-profile dropdown">

                <div class="nav-profile-text">
                    <p class="mb-1 text-black "><a class="nav-link pt-1" href="{{ route('admin.log.out') }}">Log Out</a></p>
                </div>

            </li>
            <li class="nav-item d-none d-lg-block full-screen-link">
              <a class="nav-link">
                <i class="mdi mdi-fullscreen" id="fullscreen-button"></i>
              </a>
            </li>
              </div>
            </li>
          </ul>
          <button class="navbar-toggler navbar-toggler-right d-lg-none align-self-center" type="button" data-toggle="offcanvas">
            <span class="mdi mdi-menu"></span>
          </button>
        </div>
      </nav>
      <!-- partial -->
      <div class="container-fluid page-body-wrapper">
        <!-- partial:partials/_sidebar.html -->
        <nav class="sidebar sidebar-offcanvas" id="sidebar">
          <ul class="nav">
            <li class="nav-item nav-profile">
              <a href="#" class="nav-link">
                <div class="nav-profile-image">
                  <img src="/assets/images/faces/face1.jpg" alt="profile">
                  <span class="login-status online"></span>
                  <!--change to offline or busy as needed-->
                </div>
                <div class="nav-profile-text d-flex flex-column">
                  <span class="font-weight-bold mb-2">Student</span>
                  <span class="text-secondary text-small">Student Portal</span>
                </div>
                <i class="mdi mdi-bookmark-check text-success nav-profile-badge"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ route('dashboard.teachers') }}">
                <span class="menu-title">Dashboard</span>
                <i class="mdi mdi-home menu-icon"></i>
              </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false" aria-controls="ui-basic">
                  <span class="menu-title">Students</span>
                  <i class="menu-arrow"></i>
                  <i class="mdi mdi-crosshairs-gps menu-icon"></i>
                </a>
                <div class="collapse" id="ui-basic">
                  <ul class="nav flex-column sub-menu">
                    <li class="nav-item"> <a class="nav-link" href="{{ route('students.view') }}">View Profile</a></li>
                    <li class="nav-item"> <a class="nav-link" href="{{ route('view.applications.student') }}">View Application Status</a></li>
                    <li class="nav-item"> <a class="nav-link" href="{{ route('student.note') }}">View Notice</a></li>
                    <li class="nav-item"> <a class="nav-link" href="{{ route('download.students.view') }}">View Time Table</a></li>
                    <li class="nav-item"> <a class="nav-link" href="{{ route('upload-application-student') }}">Apply for Application</a></li>
                  </ul>
                </div>
              </li>
             <div class="mt-4">
                  <div class="border-bottom">
                    <p class="text-secondary"></p>
                  </div>
                </div>
              </span>
            </li>
          </ul>
        </nav>


        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">



        <div class="card bg-light mx-auto">
            @if ($message = Session::get('success'))
            <div class="alert alert-success w-100"><strong>{{ $message }}</strong></div>
        @endif
            <article class="card-body mx-auto" style="max-width: 400px;">
                <h4 class="card-title mt-3 text-center">Create Application</h4>
                <form method="POST" action="{{ route('create.applications.student') }}" class="mx-auto" enctype="multipart/form-data">
                    @csrf
                <div class="form-group input-group">

                    <input name="name" class="w-auto form-control" placeholder="Full name" value="{{ old('name') }}" type="text">

                </div>
                @error('name')
                <div class="alert alert-danger">{{ $message }}</div>
            @enderror
                <!-- form-group// -->
                <div class="form-group input-group">

                    <input name="email" class="w-auto form-control" placeholder="Email address" type="email" value="{{ old('email') }}">

                </div> <!-- form-group// -->
                @error('email')
                <div class="alert alert-danger">{{ $message }}</div>
            @enderror
                <div class="form-group input-group">

                    <select class="custom-select" style="max-width: 120px;">
                        <option selected="">+91</option>
                    </select>
                    <input name="phonenumber" value="{{ old('phonenumber') }}" class="w-auto form-control" placeholder="Phone number" type="text">

                </div>
                @error('phonenumber')
        <div class="alert alert-danger">{{ $message }}</div>
    @enderror

    <div class="form-group input-group">

        <input class="form-control w-auto" name="subject" value="{{ old('subject') }}" placeholder="Write Subject Here" type="text">

    </div> <!-- -group// -->
    @error('subject')
    <div class="alert alert-danger">{{ $message }}</div>
@enderror


                <!-- form-group// -->
                <div class="form-group input-group">

                    <textarea class="form-control w-auto" rows="10" cols="60" name="description" value="{{ old('discription') }}" type="text">
                    </textarea>
                </div> <!-- -group// -->
                @error('discription')
                <div class="alert alert-danger">{{ $message }}</div>
            @enderror
                <!-- form-group// -->

                <div class="form-group">
                    <button type="submit" class="btn btn-primary btn-block"> Create Application  </button>
                </div> <!-- form-group// -->
            </form>
            </article>
            </div> <!-- card.// -->

            </div>





    <!-- container-scroller -->
    <!-- plugins:js -->
    <script src="/assets/vendors/js/vendor.bundle.base.js"></script>
    <!-- endinject -->
    <!-- Plugin js for this page -->
    <script src="/assets/vendors/chart.js/Chart.min.js"></script>
    <script src="/assets/js/jquery.cookie.js" type="text/javascript"></script>
    <!-- End plugin js for this page -->
    <!-- inject:js -->
    <script src="/assets/js/off-canvas.js"></script>
    <script src="/assets/js/hoverable-collapse.js"></script>
    <script src="/assets/js/misc.js"></script>
    <!-- endinject -->
    <!-- Custom js for this page -->
    <script src="/assets/js/dashboard.js"></script>
    <script src="/assets/js/todolist.js"></script>
    <!-- End custom js for this page -->


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>















